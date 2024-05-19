from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):
    return HttpResponse ('home')

def educacion (request):
    return HttpResponse ('educacion')


def experiencia (request):
    return HttpResponse ('experiencia')

def proyectos (request):
    return HttpResponse ('proyecto')

def extracurricular (request):
    return HttpResponse ('extracurricular')

def contacto (request):
    return HttpResponse ('contacto')