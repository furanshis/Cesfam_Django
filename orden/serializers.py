from rest_framework import serializers

from .models import *

from remedios.serializers import *

class OrdenRemedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = remedioOrdenado
        fields = (
            "precio",
            "remedio",
            "cantidad"
        )

class OrdenSerializer(serializers.ModelSerializer):
    items = OrdenRemedioSerializer(many=True)
    class Meta:
        model = Orden
        fields = (
            "id",
            "nombre",
            "apellido",
            "email",
            "direccion",
            "telefono",
            "stripe_token",
            "items",
            "monto_pago",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        orden = Orden.objects.create(**validated_data)

        for items_data in items_data:
            remedioOrdenado.objects.create(**validated_data)
        
        return orden