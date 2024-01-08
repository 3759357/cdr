from rest_framework import serializers
from .models import tour,restaurant

class tourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tour
        fields='__all__'

class restaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurant
        fields='__all__'