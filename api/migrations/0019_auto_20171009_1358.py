# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20171009_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='bacterium',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='decor',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='obstacle',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
