# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20171010_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bacterium',
            name='type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='obstacle',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]