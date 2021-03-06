# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VOResource_AccessURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1024)),
                ('use', models.CharField(choices=[('full', 'full'), ('base', 'base'), ('dir', 'dir')], default='full', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='VOResource_Capability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standardID', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VOResource_Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='1.0', max_length=256)),
                ('role', models.CharField(max_length=1024)),
                ('capability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VOResource_Capability')),
            ],
        ),
        migrations.AddField(
            model_name='voresource_accessurl',
            name='interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VOResource_Interface'),
        ),
    ]
