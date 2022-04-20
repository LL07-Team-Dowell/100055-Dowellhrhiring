# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def tasks_view(request):
    applications = Task.objects.all()
    serializer = TaskSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_task(request):
    serializer = TaskSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    else:
        print("Error in validating all fields!")

    return Response(serializer.data)
