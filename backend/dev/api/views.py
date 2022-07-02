from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Pipe
from .serializer import PipeSerializer

# Create your views here.
class PipeView(generics.CreateAPIView):
    queryset = Pipe.objects.all()
    serializer_class = PipeSerializer

@api_view(['GET', 'POST'])
def pipe_list(request):
    if request.method == 'GET':
        pipe = Pipe.objects.all()
        serializer = PipeSerializer(pipe, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def pipe_detail(request, pk):
    try:
        pipe = Pipe.objects.get(pk=pk)
    except Pipe.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PipeSerializer(pipe)
        # return JsonResponse(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PipeSerializer(pipe, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pipe.delete()
        return HttpResponse(status=204)

def pipe_threshold_gt(request, risk):
    risk = float(risk)
    try:
        pipe = Pipe.objects.filter(risk__gte=risk)
    except Pipe.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET': 
        serializer = PipeSerializer(pipe, many=True)
        return JsonResponse(serializer.data, safe=False)

def pipe_threshold_lt(request, risk):
    risk = float(risk)
    try:
        pipe = Pipe.objects.filter(risk__lt=risk)
    except Pipe.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET': 
        serializer = PipeSerializer(pipe, many=True)
        return JsonResponse(serializer.data, safe=False)