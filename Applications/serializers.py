from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Job, JobApplication, Meeting, Project, RehiredCandidates
# import json


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationSerializer(ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class RehiredCandidatesSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
