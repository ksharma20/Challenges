from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.ulogin, name='login'),
    path('signup/', views.uregister, name='register'),
    path('cart/', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
]
