from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Location


class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Location
        fields = ('id', 'owner', 'latitude', 'logitude', 'address', 'created', 'updated', 'retrieved')


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'locations')
