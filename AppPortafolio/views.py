from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, 'portafolioDoc/home.html')

def educacion (request):
    return render (request, 'portafolioDoc/educacion.html')


def experiencia (request):
    return render (request, 'portafolioDoc/experiencia.html')

def proyectos (request):
    return render (request, 'portafolioDoc/proyectos.html')

def extracurricular (request):
    return render (request, 'portafolioDoc/extracurricular.html')

def contacto (request):
    return render (request, 'portafolioDoc/contacto.html')