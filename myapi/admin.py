from django.contrib import admin
from .models import ApiClick

class ApiClickAdmin(admin.ModelAdmin):
    list_display = ('data', 'ip_address')  # Use os campos corretos do modelo
    ordering = ('-data',)  # Ordena por data, do mais recente para o mais antigo

admin.site.register(ApiClick, ApiClickAdmin)
