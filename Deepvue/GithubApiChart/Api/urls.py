from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('repos', views.repos),
    path('repos/<org>/<repo>/commits/', views.commits),
]