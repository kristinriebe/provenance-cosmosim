# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prov_w3c', '0002_agent_wasassociatedwith_wasattributedto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='annotation',
            new_name='docuLink',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='annotation',
            new_name='dataproduct_subtype',
        ),
        migrations.AddField(
            model_name='activity',
            name='code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='parameter',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='subtype',
            field=models.CharField(choices=[('cs:halofinding', 'cs:halofinding'), ('cs:mergertree-generation', 'cs:mergertree-generation')], max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('cs:simulation', 'cs:simulation'), ('cs:processing', 'cs:processing')], max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='dataproduct_type',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='docuLink',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]