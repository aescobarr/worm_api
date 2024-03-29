# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from api.models import WormUser, Scenario, Action, Decor, Obstacle, Bacterium, Group
from api.serializers import WormUserSerializer, ScenarioSerializer, ActionSerializer, BacteriumSerializer, DecorSerializer, ObstacleSerializer, GroupSerializer
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
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            return Response(serializer.errors, status=400)


class WormUserViewSet(VerboseCreateModelMixin, viewsets.ModelViewSet):
    queryset = WormUser.objects.all()
    serializer_class = WormUserSerializer


class GroupViewSet(VerboseCreateModelMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

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
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        if username == '' or password == '':
            raise ParseError(detail='Username and password are mandatory')

        user = get_object_or_404(User, username=username)

        user = authenticate(username=username, password=password)

        if user is not None:
            wormuser = WormUser.objects.get(user=user)
            levels = Scenario.objects.filter(user=wormuser)
            level_data = {}
            dict_list = []
            for level in levels:
                try:
                    current_points = level_data[level.level_id]
                    if level.get_points() > current_points:
                        level_data[level.level_id] = level.get_points()
                except KeyError:
                    level_data[level.level_id] = level.get_points()
                #level_data.append({"screen_id":level.level_id,"points": level.get_points()})
            for key,value in level_data.items():
                temp = {key:value}
                dict_list.append(temp)
            return Response({'user': wormuser.id, "levels": dict_list})
        else:
            raise ParseError(detail='Authentication error')
