from django.urls import path
from . import views

urlpatterns = [
    path('ramais/', views.ramais, name="ramais" )
]