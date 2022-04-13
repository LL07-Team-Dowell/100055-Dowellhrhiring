# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobApplication, Job, Meeting, Project
from .serializers import JobApplicationSerializer
from django.db.models import Q

from rest_framework.decorators import api_view
from django.conf import settings
import requests
import time
import os


def application_view(request):
    pass


def add_new_job(request):
    pass


def get_jobs(request):
    pass
