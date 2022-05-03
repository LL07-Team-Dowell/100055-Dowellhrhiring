from hashlib import algorithms_available
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
# create views here


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        #user = User.objects.filter(email=email).first()
        user = User.objects.get(email=email)
        if user is None:
            raise AuthenticationFailed("User not Found!")
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid Credentials!")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        secret_key = "DowellSecret"
        token = jwt.encode(payload, secret_key,
                           algorithm="HS256")  # .decode("utf-8")

        response = Response()

        response.data = {
            "message": "Successfully Logged In!",
            "jwt": token
        }
        return response


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
