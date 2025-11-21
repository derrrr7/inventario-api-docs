# proyecto_api/urls.py

# --- 1. PYTHON STANDARD LIBRARY IMPORTS (N/A) ---

# --- 2. THIRD-PARTY IMPORTS (Django y Librerías) ---
from django.contrib import admin
from django.urls import path, include

# Django REST Framework / drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# --- 3. CONFIGURACIÓN DEL ESQUEMA SWAGGER ---
schema_view = get_schema_view(
    openapi.Info(
        title="API Inventario Derwin Viera (v1)",
        default_version='v1',
        description="Documentación de la API RESTful para la gestión de ítems de inventario.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@ejemplo.com"),
        license=openapi.License(name="Licencia Propia"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# --- 4. URL PATTERNS ---
urlpatterns = [
    # Rutas de administración
    path('admin/', admin.site.urls),
    
    # Rutas de la API (para la app 'inventario')
    path('api/v1/', include('inventario.urls')),
    
    # Rutas de Documentación (Swagger y Redoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]