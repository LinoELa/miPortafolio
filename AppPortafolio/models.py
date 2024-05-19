from django.db import models

# Create your models here.


class infomacion_portafolio(models.Model):

    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=500)
    # crear la carpeta de medios para hacer el upload de imagenes 
    imagen = models.ImageField()


    def __int__(self): #info en modelo
        return self.titulo
    

