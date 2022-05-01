from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('machine/<pk>', views.detail),
]
