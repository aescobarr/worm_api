# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20171009_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='token_partida',
            field=models.CharField(default='', max_length=150),
        ),
    ]