# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prov_simdm', '0016_parametersetting_annotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametersetting',
            name='annotation',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
