# inventario/serializers.py

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Item, utilizado para transformar
    objetos Item a JSON y viceversa.
    """
    class Meta:
        model = Item
        fields = ('id', 'nombre', 'cantidad', 'creado_en')
        read_only_fields = ('creado_en',) # El campo 'creado_en' no se puede modificar en peticiones