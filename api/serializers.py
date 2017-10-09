from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import WormUser, Scenario, Action, Bacterium, Decor, Obstacle
import uuid


class WormUserSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email', required=True)
    password = serializers.CharField(source='user.password')

    class Meta:
        model = WormUser
        #fields = ('id', 'username', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'password')
        fields = ('id', 'wormname', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'password')

    def update(self, instance, validated_data):
        #instance.user.username = validated_data.get('user.username', instance.user.username)
        instance.user.first_name = validated_data.get('user.first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get('user.last_name', instance.user.last_name)
        instance.user.email = validated_data.get('user.email', instance.user.email)
        instance.user.password = validated_data.get('user.password', instance.user.password)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.wormname = validated_data.get('wormname', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

    def create(self, validated_data):
        user_uuid = uuid.uuid1()
        user = User.objects.create_user(username=str(user_uuid),
                                        first_name=validated_data.get('user')['first_name'],
                                        last_name=validated_data.get('user')['last_name'],
                                        email=validated_data.get('user')['email'],
                                        password=validated_data.get('user')['password'],
                                        )

        wormuser = WormUser.objects.create(birth_date=validated_data.get('birth_date'),gender=validated_data.get('gender'), wormname=validated_data.get('wormname'), user=user)
        return wormuser

    def validate_email(self,value):
        if WormUser.objects.filter(user__email=value).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("There is a user with this email address already!")
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
        fields = ('id', 'token_partida', 'world_num', 'level_num', 'user', 'scenario_size', 'scenario_size_width', 'scenario_size_height', 'speed', 'time', 'visibility', 'worm_type', 'obstacles', 'decors', 'bacteria')

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
    class Meta:
        model = Action
        fields = '__all__'