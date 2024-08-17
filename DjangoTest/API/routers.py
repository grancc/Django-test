from rest_framework import routers
from API.viewsets import *
from django.urls import path

router = routers.SimpleRouter()

router.register(r'car', CarsViewSet, basename='cars')

urlpatterns = [
    *router.urls,]