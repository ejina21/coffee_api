from rest_framework import serializers
from .models import *


class CoffeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'


class PlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    status = serializers.HiddenField(default=1)

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('number_phone', 'status')
