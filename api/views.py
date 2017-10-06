# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from api.models import WormUser, Scenario, Obstacle, Decor, Bacterium, Action
from api.serializers import WormUserSerializer, ScenarioSerializer, ObstacleSerializer, DecorSerializer, BacteriumSerializer, ActionSerializer

# Create your views here.

class WormUserViewSet(viewsets.ModelViewSet):
    queryset = WormUser.objects.all()
    serializer_class = WormUserSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class ObstacleViewSet(viewsets.ModelViewSet):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer


class DecorViewSet(viewsets.ModelViewSet):
    queryset = Decor.objects.all()
    serializer_class = DecorSerializer


class BacteriumViewSet(viewsets.ModelViewSet):
    queryset = Bacterium.objects.all()
    serializer_class = BacteriumSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer