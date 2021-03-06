# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171006_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='event',
            field=models.CharField(choices=[('turn_right', 'Turn right'), ('turn_left', 'Turn left'), ('collision', 'Player crashed against an obstacle'), ('element_viewed', 'Player discovered resource'), ('element_caught', 'Player picked up resource'), ('start', 'Player started game'), ('end', 'Player ended game')], max_length=20),
        ),
    ]
