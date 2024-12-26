from django.db import models
from django.utils.translation import gettext_lazy as _

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255, verbose_name=_("Nombre del Laboratorio"))
    ciudad = models.CharField(max_length=255, verbose_name=_("Ciudad"), default="Santiago")
    pais = models.CharField(max_length=255, verbose_name=_("País"), default="Chile")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("Laboratorio")
        verbose_name_plural = _("Laboratorios")
        ordering = ['nombre']

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255, verbose_name=_("Nombre del Director"))
    especialidad = models.CharField(max_length=255, verbose_name=_("Especialidad"), default="General")
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, verbose_name=_("Laboratorio Asociado"))

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio.nombre})"

    class Meta:
        verbose_name = _("Director General")
        verbose_name_plural = _("Directores Generales")

class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name=_("Nombre del Producto"))
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, verbose_name=_("Laboratorio"))
    f_fabricacion = models.DateField(verbose_name=_("Fecha de Fabricación"))
    p_costo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Precio de Costo"))
    p_venta = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Precio de Venta"))

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio.nombre}"

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
        ordering = ['nombre']

# Create your models here.
