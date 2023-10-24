from django.shortcuts import render
from main.models import *

# Create your views here.

def index(request):
    title = "Inicio"
    titulo_enunciado = Comunicado.titulo
    id_entidad = Entidad.id

    test = Comunicado.objects.all
    

    data = {
        'items':test,
        "title":title,
        "titulo":titulo_enunciado,
        'num_entidad':id_entidad,
    }
    return render(request,'main/index.html',data)

#def home(request):
