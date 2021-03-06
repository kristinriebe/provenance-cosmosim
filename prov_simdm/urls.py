from django.conf.urls import url
from . import views

app_name = 'prov_simdm'

urlpatterns = [
    # index view
    url(r'^$', views.IndexView.as_view(), name='index'),

    # experiments etc.
    url(r'^experiments/$', views.ExperimentsView.as_view(), name='experiments'),
    url(r'^experiments/(?P<pk>[0-9a-zA-Z.:_-]+)/$', views.ExperimentDetailView.as_view(), name='experiment_detail'),
    url(r'^experiments/(?P<pk>[0-9a-zA-Z.:_-]+)/more$', views.ExperimentMoreDetailView.as_view(), name='experiment_moredetail'),
    url(r'^protocols/$', views.ProtocolsView.as_view(), name='protocols'),
    url(r'^protocols/(?P<pk>[0-9a-zA-Z.:_-]+)/$', views.ProtocolDetailView.as_view(), name='protocol_detail'),
    url(r'^inputparameters/$', views.InputParametersView.as_view(), name='inputparameters'),
    url(r'^inputparameters/(?P<pk>[0-9a-zA-Z.:_-]+)/$', views.InputParameterDetailView.as_view(), name='inputparameter_detail'),
    url(r'^parametersettings/$', views.ParameterSettingsView.as_view(), name='parametersettings'),
    url(r'^parametersettings/(?P<pk>[0-9a-zA-Z.:_-]+)/$', views.ParameterSettingDetailView.as_view(), name='parametersetting_detail'),
    url(r'^algorithms/$', views.AlgorithmsView.as_view(), name='algorithms'),
    url(r'^algorithms/(?P<pk>[0-9a-zA-Z.:_-]+)/$', views.AlgorithmDetailView.as_view(), name='algorithm_detail'),
    url(r'^algoform/$', views.AlgorithmFormResultsView.as_view(), name='algo_form'),
    #url(r'^form/$', views.get_algorithmId, name='get_algorithmId'), # also works!
    #url(r'^form/results/$', views.AlgorithmFormResultsView.as_view(), name='algorithm_form'),

    url(r'^datasetform/$', views.DatasetFormResultsView.as_view(), name='dataset_form'),
    url(r'^datasetform_protocols/$', views.get_protocols, name='datasetform_protocols'),
    url(r'^datasetform_parameters/$', views.get_parameters, name='datasetform_parameters'),

    # provenancedm urls
    url(r'^voprov/entities/$', views.voprov_entities, name='voprov_entities'),
    url(r'^voprov/activities/$', views.voprov_activities, name='voprov_activities'),
    url(r'^voprov/activitydescriptions/$', views.voprov_activitydescriptions, name='voprov_activitydescriptions'),
    url(r'^voprov/provn/$', views.voprov_provn, name='voprov_provn'),

    # simdal urls
    url(r'^simdal/protocols/$', views.simdal_protocols, name='simdal_protocols'),
    url(r'^simdal/projects/$', views.simdal_projects, name='simdal_projects'),
    url(r'^simdal/experiments/$', views.simdal_experiments, name='simdal_experiments'),
    url(r'^simdal/datasets/$', views.simdal_datasets, name='simdal_datasets'),

    # vosi endpoints required by simdal: capabilities, availability
    url(r'^vosi/tables/$', views.vosi_tables, name='vosi_tables'),
    url(r'^vosi/tables/(?P<table_name>[0-9a-zA-Z.:_-]+)$', views.vosi_tabledetails, name='vosi_tabledetails'),
    url(r'^vosi/availability/$', views.vosi_availability, name='vosi_availability'),
    url(r'^vosi/capabilities/$', views.vosi_capabilities, name='vosi_capabilities'),

]

