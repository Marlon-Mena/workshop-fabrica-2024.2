from django.urls import path
from . import views

urlpatterns = [
    path('api_page/', views.api_page, name='api_page'),
    # outras rotas
]
