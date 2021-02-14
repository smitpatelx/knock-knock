from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('jokes/', views.create_new_joke, name="create-new-joke"),
    path('get-all-jokes/', views.get_all_jokes, name="create-new-joke"),
    path('get-random/', views.get_random_joke, name="get-random"),
    path('clear-all/', views.clear_all_jokes, name="clear-all"),
]