from django import forms
from .models import Jugador, Equipo, Estadisticas

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class EstadisticasForm(forms.ModelForm):
    class Meta:
        model = Estadisticas
        fields = '__all__'