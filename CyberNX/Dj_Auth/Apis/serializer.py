from rest_framework import serializers
from .models import User, AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["pnum", "ppic"]

class UserSerializer(serializers.ModelSerializer):
    auth_user = AuthUserSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "auth_user"]
