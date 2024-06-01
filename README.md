# miPortafolio

Voy a invertir 48h en este proyecto


### Informacion adicional 
- Voy a crear un blog  dentro de portafolio para poder ir subiendo partes de los proyecto que voy haciendo. 
- 

## Parte I
Creamos las vistas del navbar

## Parte II 
Para organizar las URLs para que cuendo tengamos otros proyectos podamos organizar mejor las url
- Usaremos 
    - - include en el path pricipal que apunte a la urls que hemos creado
    - - Include es para poder enlazar el archivo urls del proyecto con de la apliacion.

- Creamos un archivo URLs para que podamos estrucuturar mejor el codigo y las URLs. 

- Creamos la carpeta templates dentro de nuestra apliacion 
    - Dentro creamos otra carpeta con el nombre que le queremos dar a la carpeta que contenga las plantillas de html
    - Craemos las carpetas html  que son las plantillas que vamos a utilizar.

- Registramos nuestra app en proyecto,  por settings.py

- Hacer que las vistas renderizen las plantillas html creadas 
    - ya no queremos que hagan un httpresponse donde solo nos envia texto

# parte III
Bootstrap and Css

- Creamos la carpeta static 
    - Dentro creamos la carpeta css    
        - le podemos poner el nombre de la app
            - blog o portafolio .css

    - Vincular  Bootstrap  al home.html

    - Vincular style con la plantilla home.html


- EDITAR EL HTML o Navbar Principal
    - Empezamos con solo haciendo el navbar

    - las imagenes como son algo como estetaicas pues de pone directamente dentro de una carpeta llamada como sea dentro del static 
    
- Aveces para que las imagenes se cargen es mejoro hacer un coleectic de ellos,  puedo usar algo como 
    - python manage.py collectstatic

- Si no se carga las fotos puedo intentar abrir la pagian en el archivo en modo incognito. 



- - PRIMERO EN BOOTRASP : 
    - Hacer el navbar 
    - seccion 1 
    - seccion 2 
    - seccion 3 


# Parte IV 
- Formato del sitio con Bootstrap 
Vincular el sitio Web a la plantilla de bootstrap 


# Parte V_

- Creacion de plantillas (Templates)
- Herencia de plantillas  y estructura de sitios.



#### Creacion de Plantillas (Templates)
- La mejor forma es coger partes de plantillas de boostrap y ponerse hacer que se vean 

### Herencia de plantillas 
- Para que herenden las plantillas hijos (plantillas normales ) hay que crear la plantilla padre (Base.html)
    - la mejor forma es copiar la plantilla home que pegarla cambiar el nombre a base.html

- Luego crear en blog content dentro de la plantilla padre  (base.html)
    > {% block content %} (1)
    > {% endblock %} (1)

- Luego extender  la pantilla padre dentro en las pantilas hijas (home.html) 
    >{% extends 'nombredeApp/base.html' %} (2)

- luego cargar  la plantilla base.html 
    > {% load static%} (3)


- Luego creamos un block content en base.html y todo el contendo del Navbar & Footer tienen que ir dentro 
    > {% block content %} (4)
    > {% endblock %} (4)


- **Al base.html seria**

    > {% load static%}  (3)

    -- Start intro & navbar --
    -- End intro & navbar -- 


    >{% block content %} (4)
    {% endblock %} (  4)

     --- start Footer ---  
     --- end Footer ---  



- **Al home.html  & otras seria**

    > {% extend 'nombre_Carpeta_en_templates/base.html' %} (2)

    >{% load static%}  (3)

    >{% block content %} (1)
    {% endblock %} (1)



# Parte VI
- Completar las demas paginas o plantillas con la herencias de navbar  el footer

