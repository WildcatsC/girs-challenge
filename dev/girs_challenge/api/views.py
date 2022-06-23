from multiprocessing import Pipe
from django.shortcuts import render
from rest_framework import generics
from .models import Pipe
from .serializer import PipeSerializer

# Create your views here.
class PipeView(generics.CreateAPIView):
    queryset = Pipe.objects.all()
    serializer_class = PipeSerializer
