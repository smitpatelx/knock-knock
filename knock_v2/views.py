from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from knock_v2.models import (
    Joke
)
from django.utils.timezone import make_aware
from datetime import datetime
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.core.management.color import no_style
from django.db import connection, connections
import json
import pytz


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Joke):
            return str(obj)
        return super().default(obj)

"""
Send all jokes
:returns JsonResponse
"""
def get_all_jokes(request) :
    print(request)
    if request.method == 'GET' :
        all_objects = Joke.objects.all()

        if len(all_objects) > 0 :
            data = serializers.serialize('json', all_objects, cls=LazyEncoder)
            return JsonResponse(json.loads(data), status=200, safe=False)
        else :
            return JsonResponse(data={}, status=200)
    else :
        return JsonResponse(data={'message':'Request not allowed'}, status=400)

"""
Send random joke
:returns JsonResponse
"""
def get_random_joke(request) :
    if request.method == 'GET' :
        if Joke.objects.count() > 0 :
            random_data = Joke.objects.all().order_by('?')[0]
            data = serializers.serialize('json', [random_data], cls=LazyEncoder)
            return JsonResponse(json.loads(data), status=200, safe=False)
        else :
            return JsonResponse(data={}, status=200)
    else :
        return JsonResponse(data={'message':'Request not allowed'}, status=400)

"""
Clear all jokes
:return JsonResponse
"""
@csrf_exempt
def clear_all_jokes(request):
    if request.method == 'DELETE' :
        try:
            Joke.objects.all().delete()
            commands = connections["default"].ops.sequence_reset_sql(no_style(), [Joke])
            with connection.cursor() as cursor:
                for sql in commands:
                    cursor.execute(sql)
            data = {
                'message': 'All jokes deleted successfully!',
            }
            return JsonResponse(data, status=200)
        except ValueError as e:
            data = {
                'errorCode': 'ErrorDelJoke',
                'errorMessage': 'Couldn\'t delete Jokes!',
            }
            return JsonResponse(data, status=500)
    else :
        return JsonResponse(data={'message':'Request not allowed'}, status=400)

"""
Create new Joke
:return JsonResponse
"""
@csrf_exempt
def create_new_joke(request):
    if request.method == 'POST' :
        # TODO : Create new joke 
        json_data = json.loads(request.body)
        joke_content = json_data['joke_content']
        # pub_date = dateutil.parser.parse(json_data['pub_date'])
        pub_date = datetime.strptime(json_data['pub_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        pub_date = make_aware(pub_date)
        try :
            data = Joke.objects.create(joke_content=joke_content, pub_date=pub_date)
            return JsonResponse(data={'message': 'Joke saved successfully'}, status=200)
        except Exception as e :
            data={
                'message': 'Error creating new joke',
                'error':  str(e)
            }
            return JsonResponse(data, status=400)
    else :
        return JsonResponse(data={'message':'Request not allowed'}, status=400)