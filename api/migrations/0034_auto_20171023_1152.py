# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_remove_action_scenario'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='pos_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='action',
            name='pos_y',
            field=models.FloatField(default=0),
        ),
    ]
