# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class WormUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    birth_date = models.CharField(max_length=10)

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
        return self.user.email


class Scenario(models.Model):
    token_partida = models.CharField(max_length=150,unique=True)
    world_id = models.CharField(db_index=True, max_length=50)
    level_id = models.CharField(db_index=True, max_length=50)
    user = models.ForeignKey(WormUser)
    scenario_size = models.CharField(max_length=150)
    scenario_size_width = models.IntegerField()
    scenario_size_height = models.IntegerField()
    speed = models.IntegerField()
    time = models.IntegerField()
    visibility = models.IntegerField()
    worm_type = models.CharField(max_length=50)
    totalscore = models.IntegerField(default=0)
    percent_pass = models.IntegerField(default=0)

    def __str__(self):
        return str(self.token_partida)

    def get_points(self):
        max_points = 0
        actions = Action.objects.filter(event='end').filter(token_partida=self.token_partida)
        for end_action in actions:
            if end_action.points > max_points:
                max_points = end_action.points
        return max_points


class Obstacle(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.CharField(max_length=50)
    scenario = models.ForeignKey(Scenario,related_name="obstacles",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Decor(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.CharField(max_length=50)
    scenario = models.ForeignKey(Scenario, related_name="decors", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Bacterium(models.Model):
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.CharField(max_length=50)
    score = models.IntegerField()
    scenario = models.ForeignKey(Scenario, related_name="bacteria", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Action(models.Model):
    #scenario = models.ForeignKey(Scenario, related_name="actions", on_delete=models.CASCADE, null=True, blank=True)
    event = models.CharField(max_length=20)
    action_timestamp = models.IntegerField()
    time_remaining = models.FloatField()
    points = models.IntegerField(default=0)
    token_partida = models.CharField(max_length=150, default='')
