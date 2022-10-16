from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('leaderboard/<id>', views.leaderboard),
    path('quiz/<id>', views.quiz),
    path('login', views.ulogin),
    path('register', views.uregister),
]
