from rest_framework import serializers
from .models import Account, Yard
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class YardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yard
        fields = '__all__'