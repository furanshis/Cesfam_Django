from rest_framework import serializers
from .models import *

class RemedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedios
        fields = (
            "id",
            "nombreRemedio",
            "descripcionRemedio",
            "precioRemedio",
            "stockRemedio",
            "get_image",
            "get_absolute_url",
            "get_thumbnail",
            'cantidadRemedio'
        )

class CategoriaSerializer(serializers.ModelSerializer):
    remedios = RemedioSerializer(many=True)
    class Meta:
        model = CategoriaRemedio
        fields = (
            "id",
            "nombreCategoria",
            "get_absolute_url",
            'remedios',
        )