from django.urls import path
from Product import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<id>/', views.detail, name='detail'),
]
