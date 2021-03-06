# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prov_simdm', '0007_change_datetime_to_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputDataset',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('url', models.CharField(blank=True, max_length=1024, null=True)),
                ('experiment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutputDataset',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('numberOfObjects', models.IntegerField(null=True)),
                ('accessURL', models.CharField(blank=True, max_length=1024, null=True)),
                ('experiment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='InputDataObjectType',
            fields=[
                ('objecttype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='prov_simdm.ObjectType')),
                ('label', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            bases=('prov_simdm.objecttype',),
        ),
        migrations.CreateModel(
            name='OutputDataObjectType',
            fields=[
                ('objecttype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='prov_simdm.ObjectType')),
                ('label', models.CharField(blank=True, max_length=1024, null=True)),
                ('protocol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.Protocol')),
            ],
            bases=('prov_simdm.objecttype',),
        ),
        migrations.AddField(
            model_name='inputdataset',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.OutputDataset'),
        ),
        migrations.AddField(
            model_name='outputdataset',
            name='objectType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.OutputDataObjectType'),
        ),
        migrations.AddField(
            model_name='inputdataset',
            name='inputtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.InputDataObjectType'),
        ),
        migrations.AddField(
            model_name='inputdataobjecttype',
            name='definition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.OutputDataObjectType'),
        ),
        migrations.AddField(
            model_name='inputdataobjecttype',
            name='protocol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.Protocol'),
        ),
    ]
