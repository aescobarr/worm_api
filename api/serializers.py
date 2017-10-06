from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import WormUser, Scenario, Obstacle, Decor, Bacterium, Action


class WormUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = WormUser
        fields = ('id', 'username', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'password')

    def update(self, instance, validated_data):
        instance.user.username = validated_data.get('user.username', instance.user.username)
        instance.user.first_name = validated_data.get('user.first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get('user.last_name', instance.user.last_name)
        instance.user.email = validated_data.get('user.email', instance.user.email)
        instance.user.password = validated_data.get('user.password', instance.user.password)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('user')['username'],
                                        first_name=validated_data.get('user')['first_name'],
                                        last_name=validated_data.get('user')['last_name'],
                                        email=validated_data.get('user')['email'],
                                        password=validated_data.get('user')['password'],
                                        )

        wormuser = WormUser.objects.create(birth_date=validated_data.get('birth_date'),gender=validated_data.get('gender'),user=user)
        return wormuser

    def validate_email(self,value):
        if WormUser.objects.filter(user__email=value).exists():
            raise serializers.ValidationError("There is a user with this email address already!")


class BacteriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bacterium
        fields = '__all__'


class DecorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decor
        fields = '__all__'


class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacle
        fields = '__all__'


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'