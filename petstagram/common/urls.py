from django.contrib import admin
from django.urls import path, include

from petstagram.common.views import index

urlpatterns = [
    path('', index, name='index'),
]

