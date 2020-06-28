from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *



class ClientsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsProfile
        exclude = ('user', )


class ClientSerializer(serializers.ModelSerializer):
    profile = ClientsProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id','url', 'email', 'username','first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        health_conditions = None 
        if 'health_conditions' in profile_data:
            health_conditions = profile_data.pop('health_conditions')
            print('health_conditions')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        client_profile = ClientsProfile.objects.create(user=user, **profile_data)
        if health_conditions:
            client_profile.health_conditions.set(health_conditions)
        client_profile.save()
        return user


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'

class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodations
        fields = '__all__'


class UserReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservations
        exclude = ('user', )


class GetReservationSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many = True)
    accommodations = AccomodationSerializer()

    class Meta:
        model = Reservations
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservations
        fields = '__all__'
