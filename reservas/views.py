from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ActividadDeportiva

# 1. Vista para registrar una nueva actividad deportiva
def agregar_actividad(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        lugar = request.POST.get('lugar', '').strip()
        cupo_raw = request.POST.get('cupo', '').strip()

        # Validación básica de datos
        if not nombre or not lugar or not cupo_raw:
            messages.error(request, 'Por favor, complete todos los campos obligatorios.')
        else:
            try:
                cupo = int(cupo_raw)
                if cupo <= 0:
                    messages.error(request, 'El cupo debe ser un número entero positivo.')
                else:
                    # Guardar la nueva actividad en la base de datos
                    ActividadDeportiva.objects.create(
                        nombre=nombre,
                        descripcion=descripcion,
                        lugar=lugar,
                        cupo=cupo
                    )
                    messages.success(request, f'¡La actividad "{nombre}" se registró con éxito!')
                    # Redirige para limpiar el formulario y evitar reenvíos
                    return redirect('reservas:agregar_actividad')
            except ValueError:
                messages.error(request, 'El cupo ingresado debe ser un número válido.')

    return render(request, 'reservas/agregar_actividad.html')


# 2. Vista para mostrar todas las actividades deportivas
def lista_actividades(request):
    # Consulta el modelo ActividadDeportiva para obtener todas las registradas
    actividades = ActividadDeportiva.objects.all()
    contexto = {
        'actividades': actividades
    }
    return render(request, 'reservas/lista_actividades.html', contexto)


# 3. Vista para mostrar los detalles de una actividad deportiva
def detalle_actividad(request, id):
    # Obtiene la actividad o devuelve un error 404 si no existe
    actividad = get_object_or_404(ActividadDeportiva, pk=id)
    
    # También podemos traer los horarios vinculados a través de la relación inversa
    horarios = actividad.horarios.all()

    contexto = {
        'actividad': actividad,
        'horarios': horarios
    }
    return render(request, 'reservas/detalle_actividad.html', contexto)