# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prov_w3c', '0004_auto_20161004_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endTime',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startTime',
            field=models.DateField(null=True),
        ),
    ]
