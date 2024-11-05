Proyecto Django: API de intercambio y registro de usuarios
Descripción general

Este proyecto es una aplicación web desarrollada en Django para consultar y visualizar el tipo de cambio del dólar utilizando la API del Banco Central de Brasil. La aplicación ofrece funcionalidades básicas de autenticación de usuarios y muestra el tipo de cambio en gráficos interactivos. El proyecto incluye gráficos para visualizar tipos de cambio y funcionalidades básicas de CRUD.

Características

Autenticación de usuario Registro de usuario: permite que nuevos usuarios se registren creando una nueva cuenta. Inicio de sesión de usuario: los usuarios registrados pueden iniciar sesión para acceder a la funcionalidad protegida. Cierre de sesión del usuario: los usuarios autenticados pueden cerrar sesión en la cuenta.
Consulta API de Vista de Tipo de Cambio: Consulta la API del Banco Central para obtener el tipo de cambio del dólar. Gráficos interactivos: muestra el tipo de cambio en gráficos usando Chart.js para facilitar la visualización de las variaciones.
django_project/ │ ├── myapi/ │ ├── migraciones/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├─ ─ pruebas.py │ ├── urls.py │ ├── views.py │ └── templates/ │ ├── home.html │ ├── registro/ │ │ ├── login.html │ │ └── registrarse. html │ └ ── exchange_rate.html │ ├── cad_user project/ │ ├── init.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ ├── wsgi. │ ├─ ─ administrar.py └── venv/

Estructura del proyecto

Carpetas y archivos project_django/: directorio raíz del proyecto. myapi/: Aplicación Django que contiene la lógica para el tipo de cambio y la autenticación. migraciones/: Archivos de migración de bases de datos. models.py: Define el modelo ApiClick para registrar interacciones con la API. views.py: implementa vistas para mostrar el tipo de cambio y las páginas de autenticación. urls.py: define las URL de la aplicación myapi. plantillas/: Contiene plantillas HTML para representar páginas. home.html: Página de inicio con información sobre la aplicación. registro/: Plantillas para autenticación. login.html: formulario de inicio de sesión. registrarse.html: Formulario de registro. exchange_rate.html: Página para ver el tipo de cambio en gráficos. project_cad_usuario/: Configuraciones principales del proyecto Django. settings.py: configuración del proyecto, incluida la base de datos. urls.py: Configuración de las URL principales del proyecto. wsgi.py: Configuración para el servidor WSGI. administrar.py: Script de administración para comandos de Django. venv/: Entorno virtual con dependencias del proyecto.
Características en detalle
Autenticación de usuario
Registro:
URL: /register/ Página para crear una nueva cuenta de usuario. Después del registro, el usuario es redirigido a la página de inicio de sesión. Acceso:

URL: /login/ Página de autenticación de usuarios registrados. Después de iniciar sesión, el usuario es redirigido a la página de inicio. Cerrar sesión:

URL: /logout/ Permite al usuario cerrar sesión. Consulta API de vista de tipo de cambio:

URL: /api/exchange_rate/ Endpoint que consulta la API del Banco Central y devuelve el tipo de cambio del dólar en formato JSON. Visualización con Gráficos:

URL: /exchange_rate/ Página que muestra el tipo de cambio en gráficos interactivos usando Chart.js. El gráfico muestra la fluctuación del tipo de cambio a lo largo del tiempo. Instalación de Configuración y Ejecución:

Clona el repositorio y crea un entorno virtual: bash Copia el código python -m venv venv source venv/bin/activate # En Windows: venv\Scripts\activate Instalar dependencias: bash Copia el código pip install -r requisitos.txt Datos de configuración de la base de datos:

Configure las credenciales de la base de datos en el archivo settings.py. Migraciones:

Aplique las migraciones para crear las tablas de la base de datos: bash Copiar código python Manage.py makemigrations python Manage.py migrar Ejecución:

Inicie el servidor de desarrollo: bash Copiar código python Manage.py RunServer

|El servidor estará disponible en http://127.0.0.1:8000/. |
