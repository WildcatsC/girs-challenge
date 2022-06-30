from rest_framework import serializers
from .models import Pipe
from django.contrib.auth.models import User

class PipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipe
        fields = ('id', 'names', 'geometry', 'wear', 'weather', 'vegetation', 'risk')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pipe.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'passwords']