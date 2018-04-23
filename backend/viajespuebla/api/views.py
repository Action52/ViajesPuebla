from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Viaje, Profile
from api.serializers import ViajeSerializer, UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

@csrf_exempt
def viaje_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        viajes = Viaje.objects.all()
        serializer = ViajeSerializer(viajes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ViajeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def viaje_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        viaje = Viaje.objects.get(pk=pk)
    except Viaje.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ViajeSerializer(viaje)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ViajeSerializer(viaje, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        viaje.delete()
        return HttpResponse(status=204)


@csrf_exempt
def profile_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many = True)
        return JSONResponse(serializer.data, status = 200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #Display parameters
        serializer = ProfileSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def profile_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(viaje, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profile.delete()
        return HttpResponse(status=204)
