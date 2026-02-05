from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('interfazp/', views.interfaz_admin, name='interfaz_principal'),
    path('interfazu/', views.interfaz_users, name='interfaz_usuarios'),
    path('valida/', views.valida_usuarios, name='valida_usuarios')    
]