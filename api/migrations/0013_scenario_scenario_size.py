# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20171009_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='scenario_size',
            field=models.CharField(default='', max_length=150),
        ),
    ]
