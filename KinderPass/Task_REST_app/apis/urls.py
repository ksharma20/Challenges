from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('register/', views.user_register),
    path('create/', views.create_task),
    path('tasks/', views.view_tasks),
    path('task/<pk>', views.view_task),
]
