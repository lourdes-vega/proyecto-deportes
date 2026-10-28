from django.contrib import admin
from .models import ActividadDeportiva, Horario, Inscripcion

@admin.register(ActividadDeportiva)
class ActividadDeportivaAdmin(admin.ModelAdmin):
    # Consigna 4: Columnas visibles en la lista
    list_display = ('id', 'nombre', 'lugar', 'cupo')
    
    # Consigna 4: Barra de búsqueda por nombre y lugar
    search_fields = ('nombre', 'lugar')
    
    # Opcional pero suma puntos: filtro lateral
    list_filter = ('lugar',)

# Opcional: registrar los otros modelos para que el admin quede completo
@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'actividad', 'dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia', 'actividad')

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni', 'fecha_inscripcion')
    search_fields = ('nombre', 'apellido', 'dni')