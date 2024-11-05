Django Project - User Registration and Exchange API
Overview

This project is a web application developed in Django to query and view the dollar exchange rate using the Central Bank of Brazil API. The application offers basic user authentication features and displays the exchange rate in interactive charts. The project includes charts to view exchange rates and basic CRUD features.

Features

User Authentication User Registration: Allows new users to register by creating a new account. User Login: Registered users can log in to access protected features. User Logout: Authenticated users can log out of the account.
Exchange Rate View API Query: Queries the Central Bank API to obtain the dollar exchange rate. Interactive Charts: Displays the exchange rate in charts using Chart.js to make it easier to view variations.
django_project/ │ ├── myapi/ │ ├── migrations/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├─ ─ tests.py │ ├── urls.py │ ├── views.py │ └── templates/ │ ├── home.html │ ├── registration/ │ │ ├── login.html │ │ └── register.html │ └── exchange_rate.html │ ├── projeto_cad_usuario/ │ ├── init.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ ├── wsgi.py │ ├── manage.py └── venv/

Project Structure

Folders and Files projeto_django/: Project root directory. myapi/: Django application that contains the logic for the exchange rate and authentication. migrations/: Database migration files. models.py: Defines the ApiClick model to register interactions with the API. views.py: Implements the views to display the exchange rate and authentication pages. urls.py: Defines the URLs of the myapi application. templates/: Contains HTML templates to render the pages. home.html: Home page with information about the application. registration/: Templates for authentication. login.html: Login form. register.html: Registration form. exchange_rate.html: Page to display the exchange rate in graphs. projeto_cad_usuario/: Main configurations of the Django project. settings.py: Project configurations, including the database. urls.py: Configuration of the main URLs of the project. wsgi.py: Configuration for the WSGI server. manage.py: Administration script for Django commands. venv/: Virtual environment with the project dependencies.
Features in Detail
User Authentication
Registration:
URL: /register/ Page to create a new user account. After registration, the user is redirected to the login page. Login:

URL: /login/ Page for authenticating registered users. After logging in, the user is redirected to the home page. Logout:

URL: /logout/ Allows the user to end the session. Exchange Rate View API Query:

URL: /api/exchange_rate/ Endpoint that queries the Central Bank API and returns the dollar exchange rate in JSON format. Chart View:

URL: /exchange_rate/ Page that displays the exchange rate in interactive charts using Chart.js. The chart shows the exchange rate fluctuation over time. Configuration and Execution Installation:

Clone the repository and create a virtual environment: bash Copy code python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate Install the dependencies: bash Copy code pip install -r requirements.txt Database Configuration:

Set the database credentials in the settings.py file. Migrations:

Apply the migrations to create the database tables: bash Copy code python manage.py makemigrations python manage.py migrate Execution:

Start the development server: bash Copy code python manage.py runserver

|The server will be available at http://127.0.0.1:8000/. |
