from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task

class TaskView(APIView):

    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        qs = Task.objects.all()
        # qs = Task.objects.filter(user=user)
        serializer = TaskSerializer(qs, many=True,)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response({}, status=400)
