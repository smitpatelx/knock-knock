from django.db import models
from random import randint
from django.db.models import Count

class JokeManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
 
    def random_naive(self):
        return self.all().order_by('?')[0]

# Create your models here.
class Joke(models.Model):
    joke_content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    
    objects = JokeManager()
    
    def __str__(self):
        return self.joke_content