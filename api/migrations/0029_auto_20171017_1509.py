# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20171011_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='bacteria_visibility_range',
        ),
        migrations.AlterField(
            model_name='action',
            name='event',
            field=models.CharField(max_length=20),
        ),
    ]