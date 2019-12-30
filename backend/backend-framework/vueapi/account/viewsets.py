from rest_framework import viewsets
from .models import Account, Yard
from .serializers import AccountSerializer, YardSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class YardViewSet(viewsets.ModelViewSet):
    queryset = Yard.objects.all()
    serializer_class = YardSerializer