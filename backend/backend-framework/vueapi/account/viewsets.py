from rest_framework import viewsets
from .models import Account, Yard, JobType, Job
from .serializers import AccountSerializer, YardSerializer, JobTypeSerializer, JobSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class YardViewSet(viewsets.ModelViewSet):
    queryset = Yard.objects.all()
    serializer_class = YardSerializer

class JobTypeViewSet(viewsets.ModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer