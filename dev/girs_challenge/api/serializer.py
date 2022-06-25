from rest_framework import serializers
from .models import Pipe

class PipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipe
        fields = ('geometry', 'wear', 'weather', 'vegetation', 'names', 'risk', 'id')


