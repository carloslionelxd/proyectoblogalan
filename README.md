# PROYECTO FINAL
## INFORMATORIO 2023
## COMISIÓN NRO. 7 - GRUPO NRO. 6
(Agosto de 2023)

### __DESCRIPCIÓN__ 
Este proyecto fue realizado para obtener una Aplicación Web.
Para ello se utilizó el framework Django que dió la posibilidad de aplicar los conceptos teóricos y prácticos que se adquirió a lo largo del Curso del Programa de Gobierno de la Provincia del Chaco denominado Informatorio para su Cohorte 2023.
Corresopnde a la segunda parte del proceso de capacitación de los que queremos incursionar en el campo de la programación, siendo esta oportunidad el tema central de estudio la programación de aplicaciones web con lenguaje orientado a objetos Python.

### __DETALLE DE LA APLICACIÓN__
La aplicación realizada consiste en un Blog orientado al Turismo donde se pueden realizar distintas operaciones de publicación de contenidos y mantenimento de la información.
Las operaciones específicas se mencionan a contnuación:
- Lectura de contenido por parte de visitantes al sitio.
- Acceso de usuarios registrados, se da la posibilidad de registrase como usuario para interactuar con la aplicación de acuerdo a su perfil.
- Manejo de perfil colaborador que brinda al usuario registrado la capacidad de publicar contenido.
- Acceso a usuarios registrados de poder publicar comentarios sobre los posteos o publicaciones que aparecerán en el sitio.
- Capacidad de modificar los comentarios propios de cada usuario registrado con función de edición o borrado en caso de necesitarlo.
- El perfil Colaborador de los usuarios registrados permite cargar las distintas publicaciones, con el manejo del contenido tanto de texto, como imagenes y encuadrarlos en alguna categoría en particular para organizar la visualización de la información.
- Los colaboradores podrán editar o borrar sus propias publicaciones, no así el contenido de otros colaboradores, también podrán editar o borrar comentarios que merezcan cambiar su contenido para salvaguardar la integridad del sentido de correspondencia de conceptos publicados y como una forma de mantener el respeto entre usuarios y calidad de la publicación con una función de moderación.
- Capacidad del administrador general del sitio para moderar en todos los items de las publicaciones.

### PARA TENER EN CONSIDERACIÓN

__INICIO__
Se puede obtener una copia del proyecto clonando el repositorio correspondiente de este lugar.

Repositorio: https://

__PASOS DE PREPARACIÓN__
REQUISITOS:

**PODRA REALIZAR TODOS LOS CAMBIOS Y MODIFICACIONES QUE CONSIDERE CONVENIENTE PARA QUE ESTE PROYECTO LE RESULTE UTIL O PARA MEJORAR ESTE PROYECTO ORIGINAL, SOLO LE PEDIMOS QUE MENCIONE A LOS AUTORES Y AL PROGRAMA DE CAPACITACION INFORMATORIO DE LA PROVINCIA DEL CHACO.**
Integrantes:
- Alan Aquino
- Zahir Ludueño
- Carlos Barboza

Antes de comenzar se debe comprender que para trabajar en este tipo de proyecto se debe orientar al trabajo en entornos virtuales por lo que deberá contar en su computadora personal con un entorno de desarrollo para usar el lenguaje de programación Python en su versión 3.10 o superior y una interfaz de desarrollo cuya función principal será como editor de código python y funciones de administracón del conjunto de archivos que se vayan generando en el proyecto.
Recomendamos Visual Studio Code, pero puede utilizar cualquiera de su preferencia.
También deberá contar con un motor de base de datos relacionales instalado en su computadora personal, nosotros utilizamos para el proyecto MYSQL, pero puede utilizar el que sea de su preferencia ya que la facilidad de Django para trabajar con bases de datos es adaptable con un nivel de abstración tan sencilla, que el manejo de la persistencia de los datos se maneja sin inconvenientes trabajando con el mismo proyecto pudiendo cambiar el motor de base de datos sin contratiempos y en función de lo que se puede llegar a contratar al momento de realizar el deploy del proyecto.
Se recomienda tener instalado un administrador de base de datos para el producto que Ud. utilice, puede usar el de su preferencia, nosotros trabajamos con Mysql Workbench 8.0 CE, también puede hacerlo con otros como DBeaver Community que admite el manejo de varios motores de bases de datos.
Al tener instalado python tendrá el comando pip con el que podrá instalar el generador de entornos virtuales **virtualenv**
En una ventana de línea de comandos: CMD en Microsoft Windows o Terminal en un Mac o Linux:
Creamos una carpeta nueva donde generamos el entorno virtual (por ejemplo: ENTORNOS)
```
pip install virtualenv
```

Luego podrá crear un entorno apropiado utilizando :
```
virtualenv nombre_entorno (Ejemplo: virtualenv ve_proyectopropio)
```

Deberá activar su entorno virtual de trabajo recien creado ejecutando un archivo script (activate) que se encuenta en el interior de la estructura de carpetas que creo el entorno virtual.
Estando posicionados en ENTORNOS y siguiendo con el ejemplo ejecutamos el comando:
```
source ./ve_proyectopropio/Scripts/activate
```
Como resultado de esta operación, la linea de comandos mostrará un prompt que inicia con el nombre del entorno virtual activado
Ejemplo: (ve_proyecto) C:\Users\Usuario\Desktop\ENTORNOS>

Con el entorno virtual activado utilzaremos el archivo requirements.txt para instalar los paquetes necesarios que fueron utilizados en el proyecto original, asi podrá contar con todas las dependencias necesarias en las versiones correspondientes para tener el entorno adecuado y operativo.
Utilizamos el comando:
```
pip install -r requirements.txt
```
Podrá obtener información especifica de acuerdo a su sistema opetativo y version de librerias que esté utilizando para completar este comando luego de ejecutarlo, por ejemplo: 
python -m pip install -r requirement.txt

Tambien deberá tener git instalado, lo puede descargar de https://git-scm.com/

**SI NO TIENE UN USUARIO REGISTRADO EN EL SITIO WEB DE GITHUB https://github.com/ , ES UN BUEN MOMENTO PARA REGISTRARSE EN EL SITIO Y CRER UNO**
Preste atención a tener una contraseña fuerte y tambien a generar su token para poder autenticarse con posterioridad. Dispone de toda la información en la documentación del sitio de github.

**AHORA CREE UNA CARPETA NUEVA PARA ALOJAR LOS ARCHIVOS DEL PROYECTO que serán clonados con el siguiente comando y posicionese dentro:
Por ejemplo debe tener el siguiente prompt de su terminal de comandos: 
(ve_proyecto) C:\Users\Usuario\Desktop\PROYECTO>

CLONAR EL REPOSITORIO con el comando:
```
git clone https://github.com/Alan00Aquino/Proyecto-Blog.git
```

Creará una base de datos nueva con ayuda del Mysql Workbench 8.0 CE, luego de conectarse con el usuario administrador inicial root y la clave que se generó en la instalación del motor Mysql.
```
create database proyectoblog;
use proyectoblog;
```

**ULTIMAS OPERACIONES**
- Trabajará con los archivos de configuración: settings.py
- Cargará la información de conexión para el motor Mysql:
Por ejemplo:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackathon',
        'USER': 'root',
        'PASSWORD': 'laelegida',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
Fragmento de codigo extraido de https://codigofacilito.com/articulos/articulo_15_10_2019_16_52_20

Una vez que el proyecto tenga su conexión efectiva con la base de datos asignada al proyecto:
ejecutar los comandos:
- Creamos un usuario administrador para el proyecto
  ```
  python manage.py createsuperuser
  ```
  
- Preparamos los archivos para migrar los datos a la base de datos:
  ```
  python manage.py makemigrations
  ```
  
- Efectivizamos la migración de los datos a la base de datos:
  ```
  python manage.py migrate
  ```
  Esto construye las tablas en la base de datos a partir de lo modelos declarados en el proyecto.
  
- Finalmente podrá correr una instancia local del proyecto clonado en su computadora personal con el siguiente comando:
  ```
  python manage.py runserver
  ```
  Abrir un navegador de internet en la siguiente dirección:
  localhost:8000

  
