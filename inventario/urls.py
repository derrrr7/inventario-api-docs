# inventario/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

# 1. Crear el Router
router = DefaultRouter()
router.register(r'items', ItemViewSet) # Registra el ViewSet en la ruta 'items'

# 2. Definir los urlpatterns de la aplicación
urlpatterns = [
    # Incluye todas las rutas generadas por el router (list, create, retrieve, update, destroy)
    path('', include(router.urls)), 
]