from django.urls import path, include
from coffee.views import *

app_name = 'coffee'
urlpatterns = [
    path('create_coffee/', CoffeeCreateView.as_view()),
    path('create_place/', PlaceCreateView.as_view()),
    path('create_order/', OrderCreateView.as_view()),
    path('all_orders/', OrderListView.as_view()),
    path('change_order/<int:pk>/', OrderDetailView.as_view()),
]