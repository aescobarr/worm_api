# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class WormUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    birth_date = models.CharField(max_length=8,default='')

    def __repr__(self):
        return self.user.username


class Obstacle(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()


class Decor(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()


class Bacterium(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    score = models.IntegerField()


class Scenario(models.Model):
    world_num = models.IntegerField(db_index=True)
    level_num = models.IntegerField(db_index=True)
    user = models.ForeignKey(WormUser)
    scenario_size_width = models.IntegerField()
    scenario_size_height = models.IntegerField()
    speed = models.FloatField()
    worm_type = models.IntegerField()
    obstacles = models.ManyToManyField(Obstacle)
    decors = models.ManyToManyField(Decor)
    bacteria = models.ManyToManyField(Bacterium)


ACTION_CHOICES = (('turn_right','Turn right'), ('turn_left','Turn left'), ('collision','Player crashed against an obstacle'), ('element_viewed','Player discovered resource'), ('element_caught','Player picked up resource'), ('start','Player started game'), ('end', 'Player ended game'))


class Action(models.Model):
    scenario = models.ForeignKey(Scenario)
    event = models.CharField(max_length=20,choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    time_remaining = models.FloatField()
    total_points = models.IntegerField()