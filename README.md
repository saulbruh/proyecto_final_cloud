# Proyecto Final de Aplicación Web en Azure 
Saúl Medina - R00621723 - smedina1723@arecibointer.edu

## 🎯 Descripción General
¿Qué hace?

Esta aplicación web, desarrollada en Flask, permite a los usuarios crear, visualizar, completar y eliminar tareas almacenadas en una base de datos SQL Server en la nube (Azure).  Cada acción del usuario se refleja inmediatamente en la base de datos, asegurando que la información se mantenga actualizada en tiempo real.

¿A quién va dirigida?

Esta herramienta está diseñada para estudiantes, profesionales o cualquier usuario que necesite una forma sencilla de organizar tareas o actividades.  Además, sirve como proyecto educativo para mostrar cómo integrar una aplicación web, una base de datos en la nube y servicios de despliegue como Azure App Service.

¿Qué problema resuelve o qué funcionalidad ofrece?

Esta aplicación web resuelve la necesidad de organizar y gestionar tareas de forma sencilla y accesible desde cualquier navegador. Centraliza la información de tareas, eliminando la dependencia del almacenamiento local y facilitando el acceso remoto.  Además, demuestra cómo implementar una arquitectura básica de aplicación web con base de datos en la nube.


## ☁️ Servicios de Azure Utilizados
| Servicio              | Propósito dentro del proyecto                    | Gratuito en Azure for Students |
|-----------------------|--------------------------------------------------|--------------------------------|
| Azure App Service     | Ejemplo: Alojamiento de la app web               | Se utilizó B1, ya que el gratuito solo permitia 60 minutos de runtime al día                          |
| Azure SQL Database    | Ejemplo: Almacenar los datos del sistema         | ✅ Sí                          |


## 🧱 Diagrama de Arquitectura
![Diagrama](img/diagrama%20arquitectura.png)


## ⚙️ Despliegue y Configuración

### 1. Preparación Local
Antes de poder correr nuestra app, necesitamos preparar el App Service localmente y verificar que corra como necesitamos. Para verificar que esté funcionando primero tenemos que hostear nuestra base de datos, en este caso en Azure. Vamos al portal, seleccionamos SQL database y lo creamos, en este caso, con el plan incluido en nuestra cuenta de estudiante. Luego en nuestro App Service local procuramos correr nuestro ambiente virtual e instalar las dependencias requeridas listadas en el documento de requirements. Luego que tenemos todo eso cargamos las variables de entorno y procuramos que en los ajustes de nuestro servidor SQL esté habilitado nuestro IP address. Luego corremos el app como cualquier aplicación Python.

Es este caso los comandos son los siguientes:
- - -

Creación del entorno virtual
- python3 -m venv venv  

Activación del entorno virtual
- source venv/bin/activate  

Instalación de las dependencias
- pip install -r requirements.txt

Cargar las variables de entorno para poder conectarse a la base de datos.
- export SQL_SERVER="dbserverproyectoestudiante.database.windows.net"                                      
export SQL_DATABASE="proyecto_estudiante"
export SQL_USERNAME="smedina"
export SQL_PASSWORD="password"  

Correr app
- python3 app.py

### 2. Configuración en Azure
Luego de procurar que el app corriera correctamente local, es tiempo de correrla en línea, es este caso dentro de un app service en Azure. El primer paso sería crear el mismo,indicando que sería uno de linux en python con la licencia gratuita de estudiante. Tambien aprovechamos y declaramos las variables de entorno que permitiran al app service conectarse con nuestra base de datos. Luego subimos nuestro código de backend a al app service. En el siguiente paso explicamos como se realiza.

### 3. Automatización
Para que automaticamente nuestro código sea actualizado en nuestra app, podemos crear un GitHub Action que nos permitirá, cada vez que hagamos un cambio en nuestro código base, correr nuestro programa de forma automática dentro de Azure. Para preparar esto tenemos que ir al deployment center dentro de los ajustes de nuestro app service e indicar que queremos preparar un github action, solo necesitamos ingresar con nuestra cuenta y seleccionar el repo que queremos implementar en nuestra app, y listo, Azure y GitHub se encargan del resto automáticamente.

## 💻 Enlace a la Aplicación Desplegada
> [Click aquí para ver la página](https://proyectocloudsm-a7ccbrcbbbbcece6.eastus2-01.azurewebsites.net)

## 🎥 Enlace a el video de presentación
> [Ver video en Youtube](https://youtu.be/joBy-r1Mx_w)

## 💸 Estimación del Costo
![Azure pricing calculator](img/Pricing%20Calculation.png)

## 📁 Capturas del Portal de Azure
![App Service](img/App%20Service.png)
![GitHub Action](img/GitHub%20Actions%20-%20App%20Service.png)
![Variables de Entorno](img/Variables%20-%20App%20Service.png)
![Base de datos](img/Base%20Datos.png)
![Firewall base de datos](img/Reglas%20Firewall%20-%20Base%20Datos.png)

## 📘 Lecciones Aprendidas
¿Qué retos enfrentaste y cómo los resolviste?

Uno de los retos más grandes fue configurar la conexión entre la aplicación Flask y la base de datos SQL Server en Azure. Problemas con drivers ODBC, reglas de firewall y variables de entorno nos impedían conectar la app correctamente. Para solucionarlo, ajustamos la configuración del App Service, usamos el driver correcto de SQL Server y habilitamos el acceso necesario desde Azure. Otro reto importante fue automatizar el despliegue continuo con GitHub Actions y Azure App Service. Nos topamos con errores de dependencias, autenticación y configuración del runtime de Python. Para arreglarlo, actualizamos las configuraciones del workflow, ajustamos la versión de Python compatible y configuramos bien el entorno de despliegue para que la app corriera sin problemas en la nube.

¿Qué aprendiste sobre trabajar con servicios cloud?

Aprendí a desplegar y administrar aplicaciones web usando servicios cloud como Azure. También me familiaricé con la integración de bases de datos y la automatización de despliegues desde GitHub. Además, comprendí la importancia de configurar variables de entorno, implementar reglas de firewall para la seguridad y gestionar recursos en la nube.

¿Qué mejorarías en una próxima versión del proyecto?

En una próxima versión, modernizaría la interfaz gráfica para ofrecer una experiencia de usuario más intuitiva y agradable. Además, implementaría autenticación de usuarios para que cada persona pueda administrar sus tareas de forma segura. También añadiría funcionalidades avanzadas como categorías, fechas límite, notificaciones y un sistema de búsqueda o filtrado de tareas. A nivel técnico, optimizaría la estructura del proyecto con una arquitectura más escalable y mejoraría el manejo de conexiones a la base de datos para un mejor rendimiento en producción.

## 📚 Repositorio del Código
> [Enlace al repositorio de este proyecto](https://github.com/saulbruh/proyecto_final_cloud)

## 🖥️ Presentación
Se encuentra dentro del mismo código base, dentro de la carpeta llamada "img"

## 🎓 Créditos
Curso: Cloud Computing  
Profesor: Javier A. Dastas  
Universidad Interamericana de Puerto Rico – Recinto de Arecibo
