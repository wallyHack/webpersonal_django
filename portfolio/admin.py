from django.contrib import admin

from .models import Proyecto

# Register your models here.

# funcionalidad extendida para los modelos
class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

admin.site.register(Proyecto)