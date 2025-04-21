from django.db import models

class User(models.Model):
    ID = models.IntegerField(verbose_name="ID", primary_key=True)
    UserName = models.CharField(max_length=20, verbose_name="Nombre de Usuario", null=True)
    PassWord = models.CharField(max_length=20, verbose_name="Contrasena", null=True)
    Activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta: 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['ID']
        
    def __str__(self):
        return self.UserName