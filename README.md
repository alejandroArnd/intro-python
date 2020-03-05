# intro-python
Buenas! Esto es una introducción de python y django

## Ejemplos utilizados

* XML
* JSON
* CSV
* Mysql

## Django
Para instalar django en nuestra maquina usaremos:
~~~
python -m pip install Django
~~~

Antes de empezar instalamos un entorno virtual (virtualenv) ya que con ellos podemos mantener 
los paquetes de nuestro proyecto agrupados, y separados de los paquetes de otros proyectos y del sistema .

Aqui el link de los pasos de instalacion del entorno virtual : https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b

El siguiente paso es iniciar el proyecto con el siguiente comando:
~~~
django-admin startproject nombreProyecto
~~~

### Comandos utiles para django

Runserver para levantar el servidor 
~~~
python3 manage.py runserver
~~~

Check sirve para comprobar la estructura del codigo sin llegar a ejecutarse

~~~
python3 manage.py check
~~~

Inspectdb Esto examinará las tablas en la base de datos DATABASE_NAME e imprimirá para cada tabla el modelo de clase generado.

~~~
python3 manage.py inspectdb
~~~

Makemigrations comprueba os cambios que ha habido en los modelos:

~~~
python3 manage.py makemigrations
~~~

Migrate aplica los cambios ocurridos en el modelo:

~~~
python3 manage.py migrate
~~~

Si queremos cambiar de gestor de bases de datos para conservar los datos que tenemos los guardaremos en un json generado con el siguiente comando:

~~~
python3 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > datadump.json
~~~

Y para cargar este json en el nuevo gestor de base de datos :

~~~
python3 manage.py loaddata datadump.json
~~~

En caso de tener tests ejecutamos el comando test para que se ejecuten estos

~~~
python3 manage.py test
~~~
