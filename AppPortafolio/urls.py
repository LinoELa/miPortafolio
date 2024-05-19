#Creado por nosotros

from django.urls import path

from AppPortafolio import views



urlpatterns = [
    path('', views.home , name='Home' ),
    path('educacion', views.educacion , name='Educacion' ),
    path('experiencia', views.experiencia , name='Experiencia' ),
    path('proyectos', views.proyectos , name='Proyectos' ),
    path('extracurricular', views.extracurricular, name='Extracurricular' ),
    path('contacto', views.contacto, name='Contacto' ),
]

