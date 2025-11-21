# inventario/models.py

# --- 1. PYTHON STANDARD LIBRARY IMPORTS (N/A) ---

# --- 2. THIRD-PARTY IMPORTS (Django) ---
from django.db import models


# --- 3. MODELS ---
class Item(models.Model):
    """
    Modelo para representar un ítem de inventario.
    
    Campos:
    - nombre: Nombre descriptivo del ítem (CharField).
    - cantidad: Cantidad disponible en stock (IntegerField).
    - creado_en: Fecha y hora de creación (DateTime, read-only).
    """
    # CAMPOS DE LA BASE DE DATOS
    nombre = models.CharField(max_length=100, help_text="Nombre descriptivo del ítem.")
    cantidad = models.IntegerField(default=0, help_text="Cantidad disponible en stock.")
    creado_en = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Ítem de Inventario"
        verbose_name_plural = "Ítems de Inventario"
        # Opcional: ordenar los resultados por defecto
        # ordering = ['nombre'] 

    def __str__(self):
        return self.nombre