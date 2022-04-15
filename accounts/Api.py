from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom claims
        serializer = UserSerializer(self.user).data

        for keys, values in serializer.items():
            data[keys] = values
        # ...

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AddUser(APIView):
    def post(self, request):
        data = request.data
        try:
            username = data['username']
            password = data['password']
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            return Response({'Response': 'User saved Successfully'})
        except:
            return Response({'Response': 'User Already Exists'})
