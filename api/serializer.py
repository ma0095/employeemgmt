from rest_framework import serializers
from api.models import Employee
from django.contrib.auth.models import User


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['__all__']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        madel=User
        fields=["username","email","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
