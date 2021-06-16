from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Order
from rest_framework.permissions import IsAuthenticated


class CoffeeCreateView(generics.CreateAPIView):
    serializer_class = CoffeeDetailSerializer
    permission_classes = IsAuthenticated,


class PlaceCreateView(generics.CreateAPIView):
    serializer_class = PlaceDetailSerializer
    permission_classes = IsAuthenticated,


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    permission_classes = IsAuthenticated,


class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderChangeSerializer
    queryset = Order.objects.all()
    permission_classes = IsAuthenticated,
