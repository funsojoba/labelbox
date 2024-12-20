from django.urls import path
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()
routers.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = routers.urls