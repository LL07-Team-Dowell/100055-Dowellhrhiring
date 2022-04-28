from rest_framework import serializers
from .models import User
# import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
