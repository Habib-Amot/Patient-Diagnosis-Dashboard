from rest_framework import serializers
from rest_framework.serializers import Serializer


class AuthenticationSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
