from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import WormUser, Scenario, Action, Bacterium, Decor, Obstacle
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


class WormUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    email = serializers.CharField(source='user.email', required=False)
    username = serializers.CharField(source='user.username', required=True)
    password = serializers.CharField(source='user.password', required=True)
    birth_date = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = WormUser
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'password', 'username')

    def update(self, instance, validated_data):
        instance.user.first_name = validated_data.get('user.first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get('user.last_name', instance.user.last_name)
        try:
            instance.user.email = validated_data.get('user.email', instance.user.email)
        except KeyError:
            instance.user.email = ''
        instance.user.username = validated_data.get('user.username', instance.user.username)
        #instance.user.username = instance.user.email
        instance.user.password = validated_data.get('user.password', instance.user.password)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

    def create(self, validated_data):
        try:
            email = validated_data.get('user')['email']
        except KeyError:
            email = ''
        try:
            first_name = validated_data.get('user')['first_name']
        except KeyError:
            first_name = ''
        try:
            last_name = validated_data.get('user')['last_name']
        except KeyError:
            last_name = ''
        try:
            user = User.objects.create_user(username=validated_data.get('user')['username'],first_name=first_name,last_name=last_name,email=email,password=validated_data.get('user')['password'],)
        except IntegrityError as ext:
            raise serializers.ValidationError(detail=ext.message)
        wormuser = WormUser.objects.create(birth_date=validated_data.get('birth_date'),gender=validated_data.get('gender'), user=user)
        return wormuser

    def validate_username(self, value):
        #if self and self.instance and self.instance.id and WormUser.objects.filter(user__username=value).exclude(id=self.instance.id).exists():
        if WormUser.objects.filter(user__username=value).exists():
            raise serializers.ValidationError(detail="There is a user with this username already!")
        return value

    def validate_email(self,value):
        #if self and self.instance and self.instance.id and WormUser.objects.filter(user__email=value).exclude(id=self.instance.id).exists():
        if value.strip() != '' and WormUser.objects.filter(user__email=value).exists():
            raise serializers.ValidationError(detail="There is a user with this email address already!")
        return value


class BacteriumSerializer(serializers.ModelSerializer):
    scenario = serializers.StringRelatedField(many=False,read_only=True)

    class Meta:
        model = Bacterium
        fields = ('width', 'coord_y', 'coord_x', 'height', 'score', 'scenario', 'type')


class DecorSerializer(serializers.ModelSerializer):
    scenario = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Decor
        fields = ('width','coord_y','coord_x','height', 'scenario', 'type')


class ObstacleSerializer(serializers.ModelSerializer):
    scenario = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Obstacle
        fields = ('width','coord_y','coord_x','height', 'scenario', 'type')


class ScenarioSerializer(serializers.ModelSerializer):
    obstacles = ObstacleSerializer(many=True)
    decors = DecorSerializer(many=True)
    bacteria = BacteriumSerializer(many=True)

    class Meta:
        model = Scenario
        fields = ('id', 'token_partida', 'world_id', 'level_id', 'user', 'scenario_size', 'scenario_size_width', 'scenario_size_height', 'speed', 'time', 'visibility', 'worm_type', 'obstacles', 'decors', 'bacteria', 'totalscore', 'percent_pass')

    def create(self, validated_data):
        obstacles_data = validated_data.pop('obstacles')
        decors_data = validated_data.pop('decors')
        bacteria_data = validated_data.pop('bacteria')

        scenario = Scenario.objects.create(**validated_data)
        for obstacle_data in obstacles_data:
            Obstacle.objects.create(scenario=scenario, **obstacle_data)
        for decor_data in decors_data:
            Decor.objects.create(scenario=scenario, **decor_data)
        for bacterium_data in bacteria_data:
            Bacterium.objects.create(scenario=scenario, **bacterium_data)
        return scenario


class ActionSerializer(serializers.ModelSerializer):
    #token_partida = serializers.CharField(source='scenario')

    class Meta:
        model = Action
        fields = ('token_partida', 'event', 'action_timestamp', 'time_remaining', 'points', 'pos_x', 'pos_y')

    '''
    def create(self, validated_data):
        token_partida = validated_data.get('scenario')
        s = get_object_or_404(Scenario,token_partida=token_partida)
        action = Action.objects.create(
            event=validated_data.get('event'),
            action_timestamp=validated_data.get('action_timestamp'),
            time_remaining=validated_data.get('time_remaining'),
            points=validated_data.get('points'),
            scenario=s
        )
        return action
    '''