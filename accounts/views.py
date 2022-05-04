<<<<<<< HEAD
=======
from hashlib import algorithms_available
>>>>>>> backend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
<<<<<<< HEAD
=======
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
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "message": "Successfully Logged In!",
            "jwt": token
        }
        return response


class UserView(APIView):
    def get(self, request):
        # get jwt token and use it to retrieve the user
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("User is not Authenticated!")
        secret_key = "DowellSecret"

        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("User not Authenticated!")
        user = User.objects.get(id=payload['id'])
        serializer = UserSerializer(user)

        return Response(serializer.data)
>>>>>>> backend


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "Successfully Logged out"
        }
        return response


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
<<<<<<< HEAD


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
>>>>>>> backend
