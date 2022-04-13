# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobApplication, Job, Meeting, Project
from .serializers import JobApplicationSerializer, JobSerializer, JobApplicationSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def application_view(request):
    applications = JobApplication.objects.all()
    serializer = JobApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_applications(request):
    applications = JobApplication.objects.all()
    serializer = JobApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def candindateview(request):
    user = request.user
    # give access to all links that are related to a candidate


def hrview(request):
    user = request.user
    if user.is_hr():
        pass
        # give access to the links for viweing applications and creating jobs
    else:
        return Response({"message": "Yu do not have the necessary Privileges!"})


@api_view(['POST'])
def update_job(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(instance=job, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_job(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return Response("Job successfully deleted")
