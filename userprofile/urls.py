# -*- coding: utf-8 -*-
"""

"""
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
	path('accounts/profiles/<profile_id>', views.profiles,name='general_profile'),
    path('accounts/profile/', views.profile,name='profile'),
    path('', views.home,name='home'),

]
