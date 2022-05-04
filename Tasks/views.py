<<<<<<< HEAD
from functools import partial
from urllib import response
=======
>>>>>>> backend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
<<<<<<< HEAD
from .serializers import CreateTaskSerializer, UpdateTaskSerializer, AllTaskSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# from rest_framework.decorators import api_view



class TaskPost(viewsets.ViewSet):
    # permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()

    def create(self, request):
        serializer_class=CreateTaskSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(
                # created_by=request.user
            )
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = self.get_object(pk=pk) 
        serializer_class=UpdateTaskSerializer( instance, data=request.data )
        if serializer_class.is_valid():
            serializer_class.save(
                # updated_by=request.user.is_team_leader
            )
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status.HTTP_400_BAD_REQUEST)

    def get_object(self ,  queryset=None, **kwargs):
        item=self.kwargs.get('pk')
        return get_object_or_404(Task, id=item)

        
    def list(self, request):
        serializer_class=AllTaskSerializer(self.queryset, many=True)
        
        return Response(serializer_class.data)


    
# @api_view(['GET'])
# def tasks_view(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def add_new_task(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 
 
 
=======
from .serializers import TaskSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def tasks_view(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> backend
