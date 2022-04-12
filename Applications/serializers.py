from rest_framework import serializers
from .models import NewJobsApplication, HRCandidateStatus, TMCandidateStatus, AccountsCandidateStatus, JobApplication
# import json


class JobApplicationSerializer(serializers.ModelSerializer):
    # other = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = JobApplication
        fields = ['id', 'feedBack', 'freelancePlatformUrl', 'applicationName',
                  'status', 'country', 'username', 'qualification',
                  'freelancePlatform', 'others', 'applicationlvl']


class NewJobApplicationSerializer(serializers.ModelSerializer):
    # other = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = NewJobsApplication
        fields = ['id', 'feedBack', 'freelancePlatformUrl', 'applicationName',
                  'status', 'country', 'username', 'qualification',
                  'freelancePlatform', 'others', 'General_Terms_Conditions', 'Technical_Specifications', 'Payment_terms', 'Work_Flow']
    # def get_other(self,obj):
    #     print(obj.others)
    #     return json.loads(obj.others)


class HrJobs(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    feedBack = serializers.SerializerMethodField(read_only=True)
    freelancePlatformUrl = serializers.SerializerMethodField(read_only=True)
    applicationName = serializers.SerializerMethodField(read_only=True)
    freelancePlatform = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    country = serializers.SerializerMethodField(read_only=True)
    qualification = serializers.SerializerMethodField(read_only=True)
    others = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = HRCandidateStatus
        fields = ['id', 'feedBack', 'freelancePlatformUrl', 'applicationName',
                  'status', 'country', 'qualification', 'freelancePlatform', 'others']

    def get_id(self, obj):
        return str(obj.JobApplication.id)

    def get_feedBack(self, obj):
        return str(obj.JobApplication.feedBack)

    def get_freelancePlatformUrl(self, obj):
        return str(obj.JobApplication.freelancePlatformUrl)

    def get_applicationName(self, obj):
        return str(obj.JobApplication.applicationName)

    def get_status(self, obj):
        return str(obj.JobApplication.status)

    def get_country(self, obj):
        return str(obj.JobApplication.country)

    def get_qualification(self, obj):
        return str(obj.JobApplication.qualification)

    def get_others(self, obj):
        return str(obj.JobApplication.others)

    def get_freelancePlatform(self, obj):
        return str(obj.JobApplication.freelancePlatform)


class TMJobs(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    feedBack = serializers.SerializerMethodField(read_only=True)
    freelancePlatformUrl = serializers.SerializerMethodField(read_only=True)
    applicationName = serializers.SerializerMethodField(read_only=True)
    freelancePlatform = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    country = serializers.SerializerMethodField(read_only=True)
    qualification = serializers.SerializerMethodField(read_only=True)
    others = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TMCandidateStatus
        fields = ['id', 'feedBack', 'freelancePlatformUrl', 'applicationName',
                  'status', 'country', 'qualification', 'freelancePlatform', 'others']

    def get_id(self, obj):
        return str(obj.JobApplication.id)

    def get_feedBack(self, obj):
        return str(obj.JobApplication.feedBack)

    def get_freelancePlatformUrl(self, obj):
        return str(obj.JobApplication.freelancePlatformUrl)

    def get_applicationName(self, obj):
        return str(obj.JobApplication.applicationName)

    def get_status(self, obj):
        return str(obj.JobApplication.status)

    def get_country(self, obj):
        return str(obj.JobApplication.country)

    def get_qualification(self, obj):
        return str(obj.JobApplication.qualification)

    def get_others(self, obj):
        return str(obj.JobApplication.others)

    def get_freelancePlatform(self, obj):
        return str(obj.JobApplication.freelancePlatform)


class ACCJobs(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    feedBack = serializers.SerializerMethodField(read_only=True)
    freelancePlatformUrl = serializers.SerializerMethodField(read_only=True)
    applicationName = serializers.SerializerMethodField(read_only=True)
    freelancePlatform = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    country = serializers.SerializerMethodField(read_only=True)
    qualification = serializers.SerializerMethodField(read_only=True)
    others = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AccountsCandidateStatus
        fields = ['id', 'feedBack', 'freelancePlatformUrl', 'applicationName',
                  'status', 'country', 'qualification', 'freelancePlatform', 'others']

    def get_id(self, obj):
        return str(obj.JobApplication.id)

    def get_feedBack(self, obj):
        return str(obj.JobApplication.feedBack)

    def get_freelancePlatformUrl(self, obj):
        return str(obj.JobApplication.freelancePlatformUrl)

    def get_applicationName(self, obj):
        return str(obj.JobApplication.applicationName)

    def get_status(self, obj):
        return str(obj.JobApplication.status)

    def get_country(self, obj):
        return str(obj.JobApplication.country)

    def get_qualification(self, obj):
        return str(obj.JobApplication.qualification)

    def get_others(self, obj):
        return str(obj.JobApplication.others)

    def get_freelancePlatform(self, obj):
        return str(obj.JobApplication.freelancePlatform)
