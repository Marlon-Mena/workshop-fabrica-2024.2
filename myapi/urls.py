from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),  # Redireciona para a página de registro
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('api/exchange_rate/', views.exchange_rate, name='exchange_rate'),
    path('exchange_rate/', views.exchange_rate_view, name='exchange_rate'),
    # outras URLs
]


