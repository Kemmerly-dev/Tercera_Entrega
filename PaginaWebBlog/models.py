from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    conferencia = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    posicion = models.CharField(max_length=50)
    promedio_puntos = models.FloatField()
    def __str__(self):
        return self.nombre

class Estadisticas(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    temporada = models.CharField(max_length=10)
    puntos = models.IntegerField()
    asistencias = models.IntegerField()
    rebotes = models.IntegerField()
    def __str__(self):
        return f'{self.jugador.nombre} - {self.temporada}'

