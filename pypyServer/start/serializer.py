# coding: utf-8
from rest_framework import serializers

from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('name', 'sensor',  'body', 'created_at', 'status', 'author')
        