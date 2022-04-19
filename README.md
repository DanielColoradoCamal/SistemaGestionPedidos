# Sistema de gestión de pedidos. 📦
### _Sistema de gestión y tienda online_

## Stacks utilizados:
[![Django](https://img.shields.io/badge/Django-3DDC8?style=for-the-badge&logo=Python&logoColor=white&labelColor=101010)]()
[![Sqlite3](https://img.shields.io/badge/Sqlite3-1B7DC5?style=for-the-badge&logo=Sqlite&logoColor=white&labelColor=101010)]()
[![Bootstrap](https://img.shields.io/badge/bootstrap-563d7c?style=for-the-badge&logo=bootstrap&logoColor=white&labelColor=101010)]()
[![Html5](https://img.shields.io/badge/Html5-e34c26?style=for-the-badge&logo=Html5&logoColor=white&labelColor=101010)]()
[![Css3](https://img.shields.io/badge/Css3-74bce9?style=for-the-badge&logo=Css3&logoColor=white&labelColor=101010)]()

## Creado por: 🧑🏽‍💻
##### Luis Daniel Colorado Camal


## Como inicializar el proyecto

#### Clonar el proyecto.
Una vez clonado el proyecto, dentro de la carpeta raiz `ProyectoWeb`
Correr el proyecto con el comando
```sh
python3 manage.py runserver
```
Verifique la implementación navegando a la dirección de su servidor en
su navegador preferido.
```sh
127.0.0.1:8000
```
## Usuario de prueba
> Nota: Puedes usar el usuario de prueba o crear uno propio.

<br>

| Usuario | Contraseña |
| ------ | ------ |
| usuarioPrueba1 | verificacion123 |




## Rutas 

Listado de rutas disponibles.

| Views | Url |
| ------ | ------ |
| Inicio | ``http://127.0.0.1:8000/`` |
| Servicios | ``http://127.0.0.1:8000/servicios/`` |
| Tienda | ``http://127.0.0.1:8000/tienda/`` |
| Contacto | ``http://127.0.0.1:8000/contacto/`` |
| form enviado con exito | ``http://127.0.0.1:8000/contacto/?valido`` |
| form enviado sin exito | ``http://127.0.0.1:8000/contacto/?novalido`` |
| Blog | ``http://127.0.0.1:8000/blog/`` |
| filtrar categorias | ``http://127.0.0.1:8000/blog/categoria/<categoria_id>/`` |
| Registrarse | ``http://127.0.0.1:8000/autenticacion/`` |
| Politica de privacidad | ``http://127.0.0.1:8000/politica/`` |
| Legales | ``http://127.0.0.1:8000/legales/`` |
| Cookies | ``http://127.0.0.1:8000/cookies/`` |
| Admin | ``http://127.0.0.1:8000/admin/`` |
| Agregar Servicio | ``http://127.0.0.1:8000/admin/servicios/servicio/`` |
| Modificar Servicio | ``http://127.0.0.1:8000/admin/servicios/servicio/{id}/change/`` |


## Modificar datos desde pantalla admin
Crear un super usuario desde la carpeta raiz ``ProyectoWeb``si ya hiciste 
```sh
python3 manage.py runserver
````
Bastara con salirte con la tecla ``ctrl + c``
Al salir de correr el servidor crearemos un **super usuario**
```sh
python3 manage.py createsuperuser
```
Cuando te lo pida, escribe tu nombre de usuario (en minúscula, sin espacios), email y contraseña. No te preocupes si no puedes ver la contraseña que estás tecleando _así es como debe ser._ Tecléalo y pulsa intro para continuar. Luego, verás algo así (donde username y email serán los que escribiste anteriormente): 
```sh
Username: example
Email address: Username@example.com
Password:
Password (again):
Superuser created successfully.
```
Corre nuevamente el servidor
```sh
python3 manage.py runserver
```

Vuelve a tu navegador e ingresa a la ruta  ``http://127.0.0.1:8000/admin`` entra con las credenciales de **super usuario** que escogiste; verás el panel de administrador de Django.




> Nota: Este proyecto es elaborado como proyecto final del curso de **CoderHouse** Python Camada: 19360


**Software libre, Disfruta!**


