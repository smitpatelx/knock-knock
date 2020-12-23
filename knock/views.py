import requests, json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.management.color import no_style
from django.db import connection, connections
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Joke, models
from .serializers import JokeSerializer
from random import randint

@api_view(('GET',))
def jokeRandom(request):
    try:
        joke = Joke.objects.random()
        serialize = JokeSerializer(joke, many=False)
        return Response(serialize.data)
    except ValueError:
        data = {
            'errorCode': 'ErrorJokeEmpty',
            'errorMessage': "Sorry we couldn't find any jokes! But you can add one. Type <b>\"Knock Kncok\"</b>",
        }
        dump = json.dumps(data)   
        return HttpResponse(dump, content_type='application/json')

@api_view(('DELETE',))
def jokeClearAll(request):
    try:
        Joke.objects.all().delete()
        commands = connections["default"].ops.sequence_reset_sql(no_style(), [Joke])
        with connection.cursor() as cursor:
            for sql in commands:
                cursor.execute(sql)
        data = {
            'message': 'All jokes deleted successfully!',
        }
        dump = json.dumps(data)
    except ValueError:
        data = {
            'errorCode': 'ErrorDelJoke',
            'errorMessage': 'Couldn\'t delete Jokes!',
        }
        dump = json.dumps(data)
        
    return HttpResponse(dump, content_type='application/json')    


class JokeView(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
