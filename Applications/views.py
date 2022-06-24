from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import JobApplication, Job, Meeting, Project, RehiredCandidate, RejectedCandidate, Team
from .serializers import JobApplicationSerializer, JobSerializer, JobApplicationSerializer
from .serializers import MeetingSerializer, ProjectSerializer, RehiredCandidateSerializer
from .serializers import RejectedCandidateSerializer, TeamSerializer
from rest_framework.decorators import api_view
from django.shortcuts import redirect


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


@api_view(['GET'])
def get_my_applications(request):
    user = request.user
    if user is None:
        return Response({"message": "You do not have the necessary Privileges! Must be logged in"})
    applications = JobApplication.objects.filter(applicant=user)
    if applications.len() < 1:
        return Response({"message": "You do not have any applications Yet!"})
    serializer = JobApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_application(request):
    serializer = JobApplicationSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_new_job(request):
    serializer = JobSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def candindateview(request):
    user = request.user
    if user is None:
        return Response({"message": "You need to login!"})
    if user.is_hr:
        return redirect("hrview")
    if user.is_team_leader:
        # return redirect("team_lead_view")
        pass
    return Response({"message": "Welcome to candidate view page!"})
    # give access to all links that are related to a candidate


def hrview(request):
    if request is None:
        return Response({"message": "You need to login and have HR rights"})
    user = request.user
    if user.is_hr():
        return Response({"message": "Welcome to HR View. You can now create new jobs and review applications"})
        pass
        # give access to the links for viweing applications and creating jobs
    else:
        return Response({"message": "You do not have the necessary Privileges!"})


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


@api_view(['GET', 'POST'])
def meeting(request):
    if request.method == 'GET':
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def rehired_candidate(request):
    if request.method == 'GET':
        rehired_candidates = RehiredCandidate.objects.all()
        serializer = RehiredCandidateSerializer(rehired_candidates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RehiredCandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def rejected_candidate(request):
    if request.method == 'GET':
        rejected_candidates = RejectedCandidate.objects.all()
        serializer = RejectedCandidateSerializer(
            rejected_candidates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RejectedCandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def teams(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(
            teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Jobs_list_Search(request):
    # receives a search term assigned q and should be a post request
    q = request.GET.get('q')
    if request.GET.get('q') == None:
        q = ''
    jobs = Job.objects.filter(  # search functionality, have any of the below
        Q(title__icontains=q) |
        Q(skills__icontains=q) |
        Q(description__icontains=q) |
        Q(is_active__icontains=q)
    )

    if jobs is not None:
        serializer = JobSerializer(
            jobs, many=True)
        return Response(serializer.data)
    else:
        pass


@api_view(['POST'])
def Jobs_application_list_Search(request):
    # receives a search term assigned q and should be a post request
    q = request.GET.get('q')
    if request.GET.get('q') == None:
        q = ''
    jobs = Job.objects.filter(  # search functionality, have any of the below
        Q(job__title__icontains=q) |
        Q(applicant__username__icontains=q) |
        Q(status__icontains=q)
    )

    if jobs is not None:
        serializer = JobSerializer(
            jobs, many=True)
        return Response(serializer.data)
    else:
        pass
