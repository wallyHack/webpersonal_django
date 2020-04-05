from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(blank=False, null=False, max_length=100) # cadena corta
    descripcion = models.TextField(blank=True, null=False) # cadena larga
    imagen = models.ImageField(upload_to="proyectos/", null=True)
    link = models.URLField(blank=True, null=True, verbose_name='Dirección Web')
    # se añade la hora automaticamente cuando se cree por primera vez(solo al crearse)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación') # verbose_name -> es como se muestra en al admin site 
    # cada vez que se modifica
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    # ordenar los proyectos por fecha de creacion, en orden inverso(Muestra primero los proyectos agregados recientemente)
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo