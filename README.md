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



# Informacion Extra 
Grid : 
- Col-sm 
- Col-md
- Col-lg
https://getbootstrap.com/docs/4.0/layout/grid/

La clase `container col-xl-10 col-xxl-8 px-4 py-5` es una combinación de clases de Bootstrap, un popular framework de desarrollo de front-end que facilita la creación de diseños responsivos y móviles primero. Cada una de estas clases tiene un propósito específico:

1. **`container`**: Esta clase establece un contenedor centrado y con padding horizontal en el diseño. Los contenedores son los bloques básicos de un diseño de Bootstrap y se utilizan para contener, rellenar y alinear el contenido dentro de una página web.

2. **`col-xl-10`**: Esta clase define una columna que ocupa 10 de las 12 partes disponibles en el sistema de rejilla de Bootstrap cuando la pantalla es extra large (≥1200px). Esto significa que la columna ocupará aproximadamente el 83.33% del ancho del contenedor en pantallas extra grandes.

3. **`col-xxl-8`**: Similar a la anterior, esta clase define una columna que ocupa 8 de las 12 partes disponibles en el sistema de rejilla de Bootstrap cuando la pantalla es extra extra large (≥1400px). En este caso, la columna ocupará aproximadamente el 66.67% del ancho del contenedor en pantallas extra extra grandes.

4. **`px-4`**: Esta clase aplica un padding horizontal (izquierda y derecha) de `1.5rem` al elemento. La "p" significa "padding" y la "x" indica que se aplica tanto a los lados izquierdo como derecho. El número "4" es un multiplicador de la unidad de espacio base de Bootstrap.

5. **`py-5`**: Similar a la anterior, esta clase aplica un padding vertical (arriba y abajo) de `3rem` al elemento. La "p" significa "padding" y la "y" indica que se aplica tanto a la parte superior como inferior. El número "5" es un multiplicador de la unidad de espacio base de Bootstrap.


6. **`g-lg-5`**  es una clase de Bootstrap que define la cantidad de espacio (gutter) entre las columnas en un contenedor de rejilla para pantallas de tamaño grande (≥992px). Aquí está la descomposición de la clase:

- **`g`**: Indica que se está definiendo el gutter, es decir, el espacio entre las columnas en el sistema de rejilla de Bootstrap.
- **`lg`**: Significa que esta clase se aplica a pantallas grandes (large), es decir, aquellas con un ancho mayor o igual a 992 píxeles.
- **`5`**: Es el tamaño del gutter, que en este caso es un multiplicador de la unidad de espacio base de Bootstrap. Bootstrap utiliza un sistema de espaciamiento con pasos de 0.25rem, por lo que `5` se multiplica por 0.25rem, dando un gutter de 1.25rem.

7. **`text-lg-start`**  Es para indicar si el texto tiene que estar al comienzo, medio o al final 


En resumen, `g-lg-5` establece un espacio de 1.25rem entre las columnas de un contenedor de rejilla en pantallas grandes y superiores. Este espacio entre las columnas ayuda a separar visualmente los elementos y a mejorar la legibilidad y el diseño en pantallas de tamaño grande.