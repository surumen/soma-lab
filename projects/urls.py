from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('ants_and_bees/',views.ants_and_bees, name='ants_and_bees'),
]