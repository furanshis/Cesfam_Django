from django.contrib.auth.models import User
from django.db import models
from remedios.models import Remedios



# Create your models here.
class correoCliente(models.Model):
    paciente = models.CharField(max_length=100)
    correoPaciente = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.CharField(max_length=400)
    


    def __str__(self):
        return self.correoPaciente

