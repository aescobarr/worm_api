# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20171009_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scenario',
            name='visibility',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='speed',
            field=models.IntegerField(),
        ),
    ]
