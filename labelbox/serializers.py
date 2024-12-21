from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    image = serializers.FileField()
    name = serializers.CharField()
    description = serializers.CharField()
    

class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'