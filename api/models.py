# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class WormUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wormname = models.CharField(max_length=150)
    gender = models.CharField(max_length=1)
    birth_date = models.CharField(max_length=8)

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
        return self.wormname


class Scenario(models.Model):
    token_partida = models.CharField(max_length=150)
    world_num = models.IntegerField(db_index=True)
    level_num = models.IntegerField(db_index=True)
    user = models.ForeignKey(WormUser)
    scenario_size = models.CharField(max_length=150)
    scenario_size_width = models.IntegerField()
    scenario_size_height = models.IntegerField()
    speed = models.IntegerField()
    time = models.IntegerField()
    visibility = models.IntegerField()
    worm_type = models.IntegerField()

    def __str__(self):
        return str(self.token_partida)


class Obstacle(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.IntegerField()
    scenario = models.ForeignKey(Scenario,related_name="obstacles",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Decor(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.IntegerField()
    scenario = models.ForeignKey(Scenario, related_name="decors", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Bacterium(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.IntegerField()
    score = models.IntegerField()
    scenario = models.ForeignKey(Scenario, related_name="bacteria", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


ACTION_CHOICES = (('turn_right','Turn right'), ('turn_left','Turn left'), ('collision','Player crashed against an obstacle'), ('element_viewed','Player discovered resource'), ('element_caught','Player picked up resource'), ('start','Player started game'), ('end', 'Player ended game'))


class Action(models.Model):
    scenario = models.ForeignKey(Scenario, related_name="actions", on_delete=models.CASCADE)
    event = models.CharField(max_length=20,choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    time_remaining = models.FloatField()
    total_points = models.IntegerField()