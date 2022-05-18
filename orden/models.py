from django.contrib.auth.models import User
from django.db import models

from remedios.models import Remedios

# Create your models here.
class Orden(models.Model):
    user = models.ForeignKey(User, related_name="ordenes", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    monto_pago = models.IntegerField(blank=True, null=True)
    stripe_token = models.CharField(max_length=400)

    class Meta:
        ordering = ['-creacion',]

    def __str__(self):
        return self.nombre

class remedioOrdenado(models.Model):
    orden = models.ForeignKey(Orden, related_name="items", on_delete=models.CASCADE)
    remedio = models.ForeignKey(Remedios, related_name="items", on_delete=models.CASCADE)
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

