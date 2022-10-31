from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" - Email: "+str(self.email)

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" - Email: "+str(self.email)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    articulo = models.IntegerField()

    def __str__(self) -> str:
        return "Producto: "+self.nombre+" - Nro.Art: "+str(self.articulo)
