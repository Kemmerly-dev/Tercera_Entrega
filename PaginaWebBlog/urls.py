from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_equipo/', views.agregar_equipo, name='agregar_equipo'),
    path('agregar_jugador/', views.agregar_jugador, name='agregar_jugador'),
    path('agregar_estadisticas/', views.agregar_estadisticas, name='agregar_estadisticas'),
    path('buscar_jugador/', views.buscar_jugador, name='buscar_jugador'),

]