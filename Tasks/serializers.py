from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Task
# import json


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
