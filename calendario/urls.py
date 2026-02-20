from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_calendario, name='nuevo_evento'),
    path('guarda_datos/', views.guarda_evento, name='guarda')
]