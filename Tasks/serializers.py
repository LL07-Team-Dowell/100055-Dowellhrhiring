from rest_framework import serializers
from .models import Task
# import json


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'created_by','created', 'task',)



class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'updated_by','updated', 'status', 'task')

class AllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id', 'task', 'created_by', 'updated_by','status', 'created', 'updated' )
