from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    logo = models.ImageField

TIPO_CHOICES = [
    ("S", "Suspensión de actividades"),
    ("C", "Suspensión de clase"),
    ("I", "Información"),
]

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    detalle_corto = models.CharField(max_length=200)
    tipo = TIPO_CHOICES
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField
    fecha_publicacion = models.DateTimeField
    fecha_ultima_publicacion = models.DateTimeField
    publicado_por = User
    modificado_por = User