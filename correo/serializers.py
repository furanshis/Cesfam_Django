from rest_framework import serializers

from .models import *

class correoSerializer(serializers.ModelSerializer):
    class Meta:
        model = correoCliente
        fields = (
            "paciente",
            "correoPaciente",
            "asunto",
            "mensaje",
        )