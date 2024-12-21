from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, GetTaskSerializer

from .utils import CloudinaryManager



class TaskViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_description="List tasks",
        operation_summary="List tasks",
        tags=["Tasks"],
    )
    
    def get(self, request):
        tasks = Task.objects.all()
        serializer = GetTaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
        operation_description="Retrieve a task",
        operation_summary="Retrieve a task",
        tags=["Tasks"],
    )
    def retrieve(self, request, pk=None):
        task = Task.objects.get(id=pk)
        serializer = GetTaskSerializer(task)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
        operation_description="Post a task",
        operation_summary="Post a task",
        tags=["Tasks"],
        request_body=TaskSerializer,
    )
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            image = request.data['image']
            name = request.data['name']
            description = request.data['description']
            
            image_url = CloudinaryManager.upload_image(image, 'images')
        
            task = Task(
                name=name, 
                description=description, 
                image=image_url)
            task.save()
            
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)