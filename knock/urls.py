from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jokes', views.JokeView)

urlpatterns = [
    # path('', views.home, name='home'),
    path('', include(router.urls)),
    path('get-random/', views.jokeRandom, name="get-random"),
]