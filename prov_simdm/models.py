from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

PROTOCOL_TYPE_CHOICES = [
                            ('Simulation', 'Simulation'),
                            ('Analysis', 'Analysis')
                        ]

@python_2_unicode_compatible
class Party(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=128, null=True) # human readable label, firstname + lastname
    #email = models.CharField(max_length=1024, blank=True, null=True)
    #address = models.CharField(max_length=1024, blank=True, null=True)
    #telephone = models.CharField(max_length=1024, blank=True, null=True
    # own attributes:
    affiliation = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'name',
        ]
        return attributes


@python_2_unicode_compatible
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=128, null=True)
    party = models.ForeignKey("Party", null=True, on_delete=models.SET_NULL)
    experiment = models.ForeignKey("Experiment", null=True, on_delete=models.SET_NULL)
    # pointer to protocol is allowed in SimDM; makes sense here, because can be used for people responsible for certain types of code (creators)
    protocol = models.ForeignKey("Protocol", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'role',
        ]
        return attributes


@python_2_unicode_compatible
class Experiment(models.Model):
    id = models.CharField(primary_key=True, max_length=128)  # new from prov
    # simdm attributes
    executionTime = models.DateField(null=True) # == voprov:endTime
    # references
    protocol = models.ForeignKey("Protocol", null=True, on_delete=models.SET_NULL) # == voprov:activitydescription
    # inherited attributes from resource
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    #referenceURL = 
    #created = 
    # collections: appliedAlgorithm (AppliedAlgorithm), inputData (InputDataset), outputData (OutputDataset), parameter (ParameterSetting)
    # collections inherited from Resource: Contact
    # attribute inherited from Resource:
    project = models.ForeignKey("Project", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'name',
            'executionTime',
            'protocol',
            'project'
        ]
        return attributes


@python_2_unicode_compatible
class Protocol(models.Model):
    id = models.CharField(primary_key=True, max_length=128)  # new from prov
    name = models.CharField(max_length=128, blank=True, null=True) # = name of the code, not included in SimDM
    code = models.CharField(max_length=128, blank=True, null=True) # must be a URI, for downloading the code!!
    version = models.CharField(max_length=32, blank=True, null=True)
    ptype = models.CharField(name="type", max_length=128, null=True, choices=PROTOCOL_TYPE_CHOICES)
    description = models.CharField(max_length=32, blank=True, null=True)
    referenceURL = models.CharField(max_length=32, blank=True, null=True)
    #parameters = [] see InputParameter-class, which refers back to Protocol

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'name',
            'code',
            'type',
            'version',
            'description',
            'referenceURL'
        ]
        return attributes


@python_2_unicode_compatible
class AppliedAlgorithm(models.Model):
    id = models.AutoField(primary_key=True)
    algorithm = models.ForeignKey("Algorithm", null=True, on_delete=models.SET_NULL)
    experiment = models.ForeignKey("Experiment", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'algorithm',
            'experiment'
        ]
        return attributes


@python_2_unicode_compatible
class Algorithm(models.Model):
    id = models.CharField(primary_key=True, max_length=128)  # new from prov
    # This class is used in collections with AppliedAlgorithm for Experiment
    # and used directly (again as collection, contains-relationship) with protocol.
    # For modelling the relation, we therefore add here a reference to the "one"-side of the many-to-one-relationship with protocol
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    label = models.CharField(max_length=1024, blank=True, null=True) # should actually be one of the SKOS-vocabularies, = skoscocept
    protocol = models.ForeignKey("Protocol", null=True, on_delete=models.SET_NULL)  # should actually not be null!! composition-relationship!

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'name',
            'description',
            'label',
            'protocol'
        ]
        return attributes


@python_2_unicode_compatible
class InputParameter(models.Model):
    id = models.CharField(primary_key=True, max_length=128)  # new from prov
    # This is refered to as "parameter" from Protocol
    protocol = models.ForeignKey("Protocol", null=True, on_delete=models.SET_NULL)
    # additional attributes for more usefulness:
    name = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=128, null=True)  # for now: only one of ['int','float','char'] is coded
    unit = models.CharField(max_length=128, null=True)
    #ucd = models.CharField(max_length=128, null=True)
    #utype = models.CharField(max_length=128, null=True)
    #arraysize = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    # own additional parameters for nicer search form:
    minval = models.CharField(max_length=128, blank=True, null=True)
    maxval = models.CharField(max_length=128, blank=True, null=True)
    default = models.CharField(max_length=128, blank=True, null=True)


    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'name',
            'datatype',
            'description',
            'protocol'
        ]
        return attributes


@python_2_unicode_compatible
class ParameterSetting(models.Model):
    id = models.AutoField(primary_key=True)  # added for convenience
    # since parameters values could be of any type, but we cannot easily model this, 
    # a compromise was suggested for SimDM: numericValue is set if the value is double, integer, ...; stringValue is used for other cases;
    # but numericValue would be a quantity, consisting of value and unit; we simplifiy here by just using
    # a string, that contains the unit, if needed
    value = models.CharField(max_length=128, blank=True, null=True)
    inputParameter = models.ForeignKey("InputParameter", null=True, on_delete=models.SET_NULL) # not one-to-one, since there can be many instances of an experiment with its params
    experiment = models.ForeignKey("Experiment", null=True, on_delete=models.SET_NULL)
    # add annotation for being able to give more explanations
    # (e.g. if force resolution varies for low and high redshift)
    annotation = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'value',
            'inputParameter',
            'experiment'
        ]
        return attributes


@python_2_unicode_compatible
class InputDataset(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=1024, blank=True, null=True)
    # simdm attributes:
    description = models.CharField(max_length=1024, blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    # container:
    experiment = models.ForeignKey("Experiment", null=True, on_delete=models.SET_NULL)
    # references:
    product = models.ForeignKey("OutputDataset", null=True, on_delete=models.SET_NULL)
    # - rename "type" to "inputtype" because 'type' is a reserved keyword
    inputtype = models.ForeignKey("InputDataObjectType", null=True, on_delete=models.SET_NULL)
    # collection: object, of type InputDataObject; optional

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'name',
            'description',
            'url',
            'experiment',
            'product',
            'inputtype'
        ]
        return attributes


@python_2_unicode_compatible
class OutputDataset(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=1024, blank=True, null=True)
    # simdm attributes:
    numberOfObjects = models.IntegerField(null=True) # e.g. snapshot numbers
    accessURL = models.CharField(max_length=1024, blank=True, null=True)
    # container:
    experiment = models.ForeignKey("Experiment", null=True, on_delete=models.SET_NULL)
    # references:
    # objectType = models.ForeignKey("ObjectType", null=True, on_delete=models.SET_NULL)
    # using ForeignKey to ObjectTye does NOT work, since ObjectType is an abstract class
    objectType = models.ForeignKey("OutputDataObjectType", null=True, on_delete=models.SET_NULL)
    # collections:
    # object (DataObject, see below)
    # characterisation (StatisticalSummary, not implemented here)


    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'numberOfObjects',
            'accessURL',
            'experiment',
            'objectType'
        ]
        return attributes


class ObjectType(models.Model): # = abstract class
    id = models.CharField(primary_key=True, max_length=128)
    # simdm attributes:
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class InputDataObjectType(ObjectType):
    #id = models.CharField(primary_key=True, max_length=128)
    # ~ like EntityDescription!
    # examples: particles, clusters, galaxies
    label = models.CharField(max_length=1024, blank=True, null=True)
    definition = models.ForeignKey("OutputDataObjectType", null=True, on_delete=models.SET_NULL)
    protocol = models.ForeignKey("Protocol", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id


@python_2_unicode_compatible
class OutputDataObjectType(ObjectType):
    # can be a collection as well
    #id = models.CharField(primary_key=True, max_length=128)
    label = models.CharField(max_length=1024, blank=True, null=True)
    protocol = models.ForeignKey("Protocol", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id


@python_2_unicode_compatible
class DataObject(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    outputDataset = models.ForeignKey("OutputDataset", null=True, on_delete=models.SET_NULL) # many can refer to the same outputdataset
    #inputDataObject = models.ForeignKey("InputDataObject", null=True, on_delete=models.SET_NULL) # only 1-1

    def __str__(self):
        return self.id

class Property(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    dataObjectType = models.ForeignKey("OutputDataObjectType", null=True, on_delete=models.SET_NULL) # many can refer to the same outputdataset
    name = models.CharField(max_length=1024, blank=True, null=True)
    datatype = models.CharField(max_length=1024, blank=True, null=True)
    unit = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    #inputDataObject = models.ForeignKey("InputDataObject", null=True, on_delete=models.SET_NULL) # only 1-1

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'dataObjectType',
            'name',
            'datatype',
            'unit',
            'description'
        ]
        return attributes

class PropertyValue(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=128, blank=True, null=True)
    property = models.ForeignKey("Property", null=True, on_delete=models.SET_NULL) # not one-to-one, since there can be many instances of an experiment with its params
    dataObject = models.ForeignKey("DataObject", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id

    def get_viewattributes(self):
        attributes = [
            'id',
            'value',
            'property',
            'dataObject'
        ]
        return attributes


@python_2_unicode_compatible
class InputDataObject(models.Model):
    # This class connects InputDataset and DataObject. 
    # It allows to specify only a subset of an outputDataset that was actually 
    # used as input for something else, by providing a link to DataObject.
    # An OutputDataset consists of DataObject, an InputDataset consists of InputDataObjects that refer to DataObjects.
    # 
    # Thus it serves as a protection 
    # layer against composition-destruction, i.e. inputDataset can contain many 
    # InputDataObjects, which themselves link (1-1) to data objects.
    # Each dataObject can be part of 1 OutputDataset.
    # If the InputDataset is destroyed, the InputDataObject would also be destroyed, 
    # but the DataObject would stay untouched.
    id = models.AutoField(primary_key=True)
    inputDataset = models.ForeignKey("InputDataset", null=True, on_delete=models.SET_NULL) # many can refer to the same inputdataset
    # renamed object to dataobject
    dataObject = models.ForeignKey("DataObject", null=True, on_delete=models.SET_NULL) # only 1-1

    def __str__(self):
        return self.id


@python_2_unicode_compatible
class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    referenceURL = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.id
