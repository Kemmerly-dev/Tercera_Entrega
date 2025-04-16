from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import EquipoForm, JugadorForm, EstadisticaForm
from .models import Jugador, Equipo, Estadistica

def inicio(request):
    return render(request, 'PaginaWebBlog/inicio.html')

def agregar_equipo(request):  # Vista equipo
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo equipo
    else:
        form = EquipoForm()
    equipos = Equipo.objects.all()
    return render(request, 'PaginaWebBlog/agregar_equipo.html', {'form': form, 'equipos': equipos})


def agregar_jugador(request):  # Vista jugador
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo jugador
    else:
        form = JugadorForm()
    jugadores = Jugador.objects.all()
    return render(request, 'PaginaWebBlog/agregar_jugador.html', {'form': form, 'jugadores': jugadores})

    
def agregar_estadisticas(request):  # Vista estadísticas
    if request.method == 'POST':
        form = EstadisticaForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar las nuevas estadísticas
    else:
        form = EstadisticaForm()
    estadisticas = Estadistica.objects.all()
    return render(request, 'PaginaWebBlog/agregar_estadisticas.html', {'form': form, 'estadistica': estadisticas})

    
def buscar_jugador(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Jugador.objects.filter(nombre__icontains=query)
    return render(request, 'PaginaWebBlog/buscar_jugador.html', {'resultados': resultados, 'query': query})



