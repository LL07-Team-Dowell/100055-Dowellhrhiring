from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .seriallizers import ProfileSerializer , UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom claims
        serializer = UserSerializer(self.user).data

        for keys , values in serializer.items():
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
            user = User.objects.create_user(username = username , password = password)
            user.save()
            return Response({'Response' : 'User saved Successfully'})
        except:
            return Response({'Response' : 'User Already Exists'})

class AddProfile(APIView):
    def post(self, request):
        data = request.data
        image = data['image'] #code to be commented
        status = data['status']
        position = data['position']
        profile = Profile(image = image, status = status, user = request.user, position = position) #code to be commented
        profile.save()
        return Response({'Response' : 'User Profile saved Successfully'})

class UpdateStatus(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        userProfile = Profile.objects.filter(user = user)

        userProfile = userProfile[0]
        if userProfile.position > 0:

            applicantProfile = Profile.objects.filter(id  = data['id'])[0]
            applicantProfile.status = data['status']
            applicantProfile.save()
            ProfileData = Profile.objects.all()

            serialliedProfileData = ProfileSerializer(ProfileData, many = True)
            print(serialliedProfileData.data)
            return Response(serialliedProfileData .data)







