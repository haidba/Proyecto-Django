from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Familiar, Estudiante

# Create your views here.

def saludar(request):
    return HttpResponse("Hola, como estas?")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola, como estas {nombre.capitalize()}'")

def mostrar_template(request):
    context= {}

    if request.GET:
        context["nombre"]= request.GET ["nombre"]
    if request.GET:
        context["apellido"]= request.GET["apellido"]
    return render(request, "mi_app/index.html", context)

def mostrar_familia(request):
    context={}
    context ["familiar"] = Familiar.objects.all()
    return render(request, 'mi_app/familiares.html', context)

def listar_estudiantes(request):
    context = {}
    context ["estudiante"] = Estudiante.objects.all()

    return render(request, 'mi_app/lista_estudiante.html', context)



