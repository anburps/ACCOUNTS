from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()
from .models import *

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,validators=[validate_password])
    conform_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        password = attrs.get('password')
        conform_password = attrs.get('conform_password')
        if password != conform_password:
            raise serializers.ValidationError("Password and conform password doesn't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('conform_password')
        user = User.objects.create_user(**validated_data)
        return user