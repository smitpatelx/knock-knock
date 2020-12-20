from django.db import models

# Create your models here.
class Joke(models.Model):
    joke_content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.joke_content