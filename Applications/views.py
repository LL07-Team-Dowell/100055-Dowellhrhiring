# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobApplication, NewJobsApplication, HRCandidateStatus, TMCandidateStatus, AccountsCandidateStatus, InternetSpeed
from accounts.models import Profile
from .serializers import JobApplicationSerializer, HrJobs, TMJobs, ACCJobs, NewJobApplicationSerializer
from django.db.models import Q

from rest_framework.decorators import api_view
from django.conf import settings
import requests
import time
import os


class ApplicationView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        user = request.user
        Application = JobApplication(applicationName=data['application'], feedBack=data['feedBack'],  others=data['others'], freelancePlatformUrl=data['url'],
                                     freelancePlatform=data['freelance'], country=data['country'], username=data['user'], qualification=data['edu'], user=user)
        Application.save()
        status = HRCandidateStatus(JobApplication=Application)
        status.save()
        return Response({'Response': 'Saved'})

    def get(self, request):
        data = JobApplication.objects.all().values('applicationName').distinct()
        # serializedData = JobApplicationSerializer(data , many = True)
        return Response(data)


class AddNewJobs(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        print(type(data['others']))

        NewJob = NewJobsApplication(applicationName=data['application'], feedBack=data['feedBack'],  others=data['others'], freelancePlatformUrl=data['url'],
                                    freelancePlatform=data['freelance'], country=data['country'], username=data['user'], qualification=data['edu'])
        NewJob.save()
        return Response({'Response': 'Saved'})

    def get(self, request):
        data = NewJobsApplication.objects.all()
        serializedData = NewJobApplicationSerializer(data, many=True)
        data = data.values('applicationName').distinct()
        return Response(serializedData.data)


class GetJobs(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        jobs = JobApplication.objects.filter(applicationName=data['name'])
        jobsData = JobApplicationSerializer(jobs, many=True)
        return Response({'res': jobsData.data})

    def get(self, request):
        user = request.user
        jobs = JobApplication.objects.filter(user=user)
        jobsData = JobApplicationSerializer(jobs, many=True)
        return Response({'res': jobsData.data})


class UpdateHRStatus(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        userProfile = Profile.objects.get(user=user)
        if userProfile.position == "HR":

            hRCanidateStatus = HRCandidateStatus.objects.get(
                JobApplication=data['id'])
            hRCanidateStatus.hr_Status = data['status']
            hRCanidateStatus.hr_FeedBack = data['feedback']
            hRCanidateStatus.save()

            if data['status'] == 'Approved':

                tMCanidateStatus = TMCandidateStatus(
                    JobApplication=hRCanidateStatus.JobApplication)
                tMCanidateStatus.save()

            return Response({'res': "Update"})
        else:
            return Response({'res': "You do not have previllage to proccess this request'"})

    def get(self, request):
        user = request.user
        userProfile = Profile.objects.get(user=user)

        if userProfile.position == "HR":
            applications = HRCandidateStatus.objects.filter(
                ~Q(hr_Status='selected'), ~Q(hr_Status='rejected'))
            data = HrJobs(applications, many=True)
            print(data.data)
            return Response({'res': data.data})


class UpdateTMStatus(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        userProfile = Profile.objects.get(user=user)

        if userProfile.position == "HR":

            tMCanidateStatus = TMCandidateStatus.objects.get(
                JobApplication=data['id'])
            tMCanidateStatus.team_lead_status = data['status']
            tMCanidateStatus.team_lead_feedback = data['feedback']
            tMCanidateStatus.save()

            if data['status'] == 'Approved':
                accountsCanidateStatus = AccountsCandidateStatus(
                    JobApplication=tMCanidateStatus.JobApplication)
                accountsCanidateStatus.save()

            return Response({'res': "Update"})
        else:
            return Response({'res': "You do not have previllage to proccess this request'"})

    def get(self, request):
        user = request.user

        userProfile = Profile.objects.get(user=user)
        hRCanidateStatus = JobApplication.objects.filter(
            applicationName=userProfile.JobTitle)
        proccessed_Jobs = HRCandidateStatus.objects.filter(
            JobApplication__in=hRCanidateStatus)
        jobs = proccessed_Jobs.filter(
            ~Q(team_lead_status='selected'), ~Q(team_lead_status='rejected'))
        data = TMJobs(jobs, many=True)
        return Response({'res': data.data})


class UpdateaACStatus(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        userProfile = Profile.objects.get(user=user)

        if userProfile.position == "HR":

            accountsCanidateStatus = AccountsCandidateStatus.objects.get(
                JobApplication=data['id'])
            accountsCanidateStatus.accounts_status = data['status']
            accountsCanidateStatus.accounts_feedback = data['feedback']
            accountsCanidateStatus.save()
            return Response({'res': "Update"})

        else:
            return Response({'res': "You do not have previllage to proccess this request'"})

    def get(self, request):
        applications = AccountsCandidateStatus.objects.filter(
            ~Q(accounts_status='selected'), ~Q(accounts_status='rejected'))
        data = ACCJobs(applications, many=True)
        return Response({'res': data.data})


class NetworkSpeedView(APIView):
    def download_speed(self):
        url = "http://speedtest.ftp.otenet.gr/files/test100k.db"
        start = time.time()
        file = requests.get(url)
        end = time.time()
        time_difference = end - start
        file_size = int(file.headers['Content-Length'])/(1000 * 100)
        download_speed = file_size / time_difference
        return round(download_speed, 2)

    def upload_speed(self):
        start = time.time()
        dummy_file = os.path.join(settings.BASE_DIR, 'dummy.txt')
        post_url = 'http://httpbin.org/post'
        with open(dummy_file, 'wb') as dummy:
            for i in range(1500):
                dummy.write(str.encode(
                    'This is a dummy text. Its sole propose is being uploaded to a server. '))
            dummy.close()
        files = {'file': open(dummy_file, 'rb')}
        request = requests.post(post_url, data=files)
        file_size = int(request.headers['Content-Length'])/(1000 * 1000)
        end = time.time()
        time_difference = end - start
        upload_speed = file_size / time_difference
        return round(upload_speed, 2)

    def get(self, request):
        user = request.user
        intenet_speed = InternetSpeed(
            user="user1", download_speed=f"{self.download_speed()}Mbps", upload_speed=f"{self.upload_speed()}Mbps")
        intenet_speed.save()
        return Response({'download_speed': f"{self.download_speed()}Mbps", 'upload_speed': f"{self.upload_speed()}Mbps"})
