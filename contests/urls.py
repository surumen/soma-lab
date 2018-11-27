# -*- coding: utf-8 -*-

from django.urls import path,include
from . import views

urlpatterns = [
    path('<contest_id>/<question_id>/', views.contest_question, name="contest_question"),
    path('<contest_id>/leaderboard/', views.leaderboard, name="contest_leaderboard"),
    path('<contest_id>/', views.contest,name="contest_detail"),
    path('', views.contests,name="contests"),
    path('contest_test/', views.contest_test,name='contest_test'),
]
