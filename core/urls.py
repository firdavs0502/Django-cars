from django.urls import path
from .views import bir

urlpatterns = [
    path('bir/', bir),
]