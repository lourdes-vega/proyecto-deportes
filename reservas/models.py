from django.db import models

# Create your models here.
class ActividadDeportiva(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    lugar = models.CharField(max_length=150)
    cupo = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - Cupo: {self.cupo}"


class Horario(models.Model):
    actividad = models.ForeignKey(ActividadDeportiva, on_delete=models.CASCADE, related_name='horarios')
    dias_semana = [
        ('lunes', 'lunes'),
        ('martes', 'martes'),
        ('miercoles', 'miercoles'),
        ('jueves', 'jueves'),
        ('viernes', 'viernes'),
        ('sabado', 'sabado'),
        ('domingo', 'domingo'),
    ]
    dia = models.CharField(max_length=10 , choices=dias_semana)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.actividad} - dia: {self.dia}"


class Inscripcion(models.Model):
    nombre= models.CharField(max_length=15 )
    apellido= models.CharField(max_length=8)
    dni = models.CharField(max_length=15)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True) #lo guarda automatico cuando se incribe 
    estados=[
        ('activo','activo'),
        ('inactivo','inactivo'),

    ]
    estado = models.CharField(max_length=10, default='activa' ,choices=estados)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dni} - fecha inscripcion : {self.fecha_inscripcion} - nombre :{self.nombre} apellido :{self.apellido}"