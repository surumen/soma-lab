# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [

    path('', views.all_tracks , name='alltracks'),
    path('(?P<pk>\d+)/', views.QuestionDetail.as_view(template_name='question_detail.html'), name="question-detail"),
    path('test/', views.test,name="test"),
    path('tracks/(?P<id>\d+)/', views.track,name="track"),
    path('allquestions/', views.QuestionList.as_view(template_name='question_list.html'),name="allquestions"),
    path('leaderboard/', views.leaderboard,name="leaderboard")

]
