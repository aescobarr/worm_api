# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from api.models import WormUser, Scenario, Action, Decor, Obstacle, Bacterium
from api.serializers import WormUserSerializer, ScenarioSerializer, ActionSerializer, BacteriumSerializer, DecorSerializer, ObstacleSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response


class VerboseCreateModelMixin(object):
    """
    Create a model instance and return either created object or the validation errors.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response(serializer.errors, status=400)


class WormUserViewSet(VerboseCreateModelMixin, viewsets.ModelViewSet):
    queryset = WormUser.objects.all()
    serializer_class = WormUserSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ScenarioViewSet, self).get_serializer(*args, **kwargs)


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

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ActionViewSet, self).get_serializer(*args, **kwargs)


@api_view(['POST'])
def api_login(request):
    if request.method == 'POST':
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        if email == '' or password == '':
            raise ParseError(detail='Email and password are mandatory')

        user = get_object_or_404(User, email=email)

        user = authenticate(username=user.username, password=password)

        if user is not None:
            wormuser = WormUser.objects.get(user=user)
            levels = Scenario.objects.filter(user=wormuser)
            level_data = []
            for level in levels:
                level_data.append({"screen_id":level.id,"points": level.get_points()})
            return Response({'user': wormuser.id, "levels": level_data})
        else:
            raise ParseError(detail='Authentication error')