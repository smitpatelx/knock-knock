import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Joke
from .serializers import JokeSerializer

class JokeView(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

# Create your views here.
# def home(request):
#     return render(request, 'jokeIndex.html')

# def create_joke(request):
#     joke_content = requests.post('joke_content')

#     return joke_content