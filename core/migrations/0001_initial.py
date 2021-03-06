# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAP_SCHEMA_columns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=256)),
                ('column_name', models.CharField(max_length=256)),
                ('datatype', models.CharField(max_length=256)),
                ('arraysize', models.IntegerField(null=True)),
                ('size', models.IntegerField(null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('utype', models.CharField(blank=True, max_length=256, null=True)),
                ('unit', models.CharField(blank=True, max_length=256, null=True)),
                ('ucd', models.CharField(blank=True, max_length=256, null=True)),
                ('indexed', models.BooleanField(default=False)),
                ('principal', models.BooleanField(default=True)),
                ('std', models.BooleanField(default=False)),
                ('column_index', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TAP_SCHEMA_key_columns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_id', models.CharField(max_length=256)),
                ('from_column', models.CharField(max_length=256)),
                ('target_column', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TAP_SCHEMA_keys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_id', models.CharField(max_length=256)),
                ('from_table', models.CharField(max_length=256)),
                ('target_table', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('utype', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TAP_SCHEMA_schemas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=256)),
                ('utype', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TAP_SCHEMA_tables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=256)),
                ('table_name', models.CharField(max_length=256)),
                ('table_type', models.CharField(max_length=256)),
                ('utype', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('table_index', models.IntegerField(null=True)),
            ],
        ),
    ]
