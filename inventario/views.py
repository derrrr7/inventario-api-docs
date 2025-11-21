# inventario/views.py

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    Endpoint para la gestión de Ítems de Inventario.

    Provee las siguientes operaciones REST:
    - **GET /inventario/items/**: Listar todos los ítems.
    - **POST /inventario/items/**: Crear un nuevo ítem.
    - **GET /inventario/items/{id}/**: Obtener detalles de un ítem.
    - **PUT/PATCH /inventario/items/{id}/**: Actualizar un ítem.
    - **DELETE /inventario/items/{id}/**: Eliminar un ítem.
    """
    queryset = Item.objects.all().order_by('nombre')
    serializer_class = ItemSerializer
    
    # Nota: El docstring de la clase es suficiente para generar toda la documentación
    # de los métodos del ViewSet, cumpliendo con el requisito de documentación básica.