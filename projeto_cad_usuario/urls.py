from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapi import views as myapi_views  # Importa as views da aplicação myapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),  # Incluindo URLs da aplicação myapi
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', myapi_views.register, name='register'),  # URL para registro
]





