from django import forms
from .models import Jugador, Equipo, Estadistica

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class EstadisticaForm(forms.ModelForm):
    class Meta:
        model = Estadistica
        fields = '__all__'