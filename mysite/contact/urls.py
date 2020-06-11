# from django.urls import re_path, include
from django.urls import path
from .views import contactView, successView

urlpatterns = [
    path('', contactView, name='contact'),
    path('success/', successView, name='success'),
]
