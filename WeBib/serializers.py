from rest_framework import serializers
from .models import Visit
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email']


#class VisitSerializer(serializers.Serializer):
    #visit_count = serializers.IntegerField()

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('count',)