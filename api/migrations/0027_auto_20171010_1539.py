# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20171010_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='bacteria_visibility_range',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scenario',
            name='percent_pass',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scenario',
            name='totalscore',
            field=models.IntegerField(default=0),
        ),
    ]