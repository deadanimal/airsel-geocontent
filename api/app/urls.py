# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('user/', views.user, name='user'),
    path('role/', views.role, name='role'),
    path('map/', views.map, name='map'),
    path('map/<str:id>/', views.map_edit, name='map_edit'),
    path('api/', views.api, name='api'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
