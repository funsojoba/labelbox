from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer



class TaskViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_description="List tasks",
        operation_summary="List tasks",
        tags=["Tasks"],
    )
    
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(
        operation_description="Retrieve a task",
        operation_summary="Retrieve a task",
        tags=["Tasks"],
    )
    def retrieve(self, request, pk=None):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)