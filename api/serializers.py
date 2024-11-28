from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['Cliente_id', 'Edad', 'Saldo', 'Activo', 'Nivel_de_Satisfaccion','Genero']
