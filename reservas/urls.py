from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    # 1. Vista para registrar nueva actividad
    path('actividades/agregar/', views.agregar_actividad, name='agregar_actividad'),
    
    # 2. Vista para mostrar todas las actividades
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    
    # 3. Vista para mostrar detalle de una actividad (con parámetro id)
    path('actividades/<int:id>/', views.detalle_actividad, name='detalle_actividad'),
]