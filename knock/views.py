import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Joke, models
from .serializers import JokeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randint

@api_view(('GET',))
def jokeRandom(request):
    try:
        joke = Joke.objects.random()
        serialize = JokeSerializer(joke, many=False)
    except ValueError:
        joke = Joke.objects.none()
        serialize = JokeSerializer(joke, many=False)    
        
    return Response(serialize.data)

class JokeView(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
