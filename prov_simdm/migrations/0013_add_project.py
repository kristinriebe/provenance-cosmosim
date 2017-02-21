# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prov_simdm', '0012_add_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('referenceURL', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prov_simdm.Project'),
        ),
    ]