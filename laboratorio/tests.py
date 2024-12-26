from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Producto, Laboratorio, DirectorGeneral

class ProductoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.laboratorio = Laboratorio.objects.create(nombre="Laboratorio Andes", ciudad="Santiago", pais="Chile")
        self.producto = Producto.objects.create(
            nombre="Aspirina", laboratorio=self.laboratorio, f_fabricacion="2024-01-01", p_costo=1000, p_venta=1500
        )

    def test_acceso_producto_lista(self):
        response = self.client.get(reverse('laboratorio:producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aspirina")

    def test_acceso_creacion_producto(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('laboratorio:producto_add'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Agregar Producto")


# Create your tests here.
