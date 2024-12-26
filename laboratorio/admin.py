from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'laboratorio']
    search_fields = ['nombre']
    list_filter = ['laboratorio']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    search_fields = ['nombre']
    list_filter = ['laboratorio', 'f_fabricacion']
# Register your models here.
