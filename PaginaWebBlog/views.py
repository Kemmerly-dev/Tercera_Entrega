from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import EquipoForm, JugadorForm, EstadisticasForm
from .models import Jugador

def inicio(request):
    return render(request, 'inicio.html') 

def agregar_equipo(request):# Vista equipo
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EquipoForm()
    return render(request, 'PaginaWebBlog/agregar_equipo.html', {'form': form})

def agregar_jugador(request):# Vista jugador
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = JugadorForm()
    return render(request, 'PaginaWebBlog/agregar_jugador.html', {'form': form})
    
def agregar_estadisticas(request):# Vista estadísticas
    if request.method == 'POST':
        form = EstadisticasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EstadisticasForm()
    return render(request, 'PaginaWebBlog/agregar_estadisticas.html', {'form': form})
    

