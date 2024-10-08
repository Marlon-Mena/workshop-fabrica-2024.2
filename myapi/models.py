from django.db import models

class ApiClick(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    
    def __str__(self):
        return f"{self.ip_address} - {self.data}"
