# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prov_simdm', '0005_auto_20170119_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedalgorithm',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
