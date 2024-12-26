from django.urls import path
from .views import (
    index,
    ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    LaboratorioListView, LaboratorioDetailView, LaboratorioCreateView, LaboratorioUpdateView, LaboratorioDeleteView,
    DirectorGeneralListView, DirectorGeneralDetailView, DirectorGeneralCreateView, DirectorGeneralUpdateView, DirectorGeneralDeleteView,
)
from django.contrib.auth.decorators import login_required, user_passes_test

def admin_required(user):
    return user.is_staff

app_name = "laboratorio"

urlpatterns = [
    path('', login_required(index), name="index"),
    path('productos/', ProductoListView.as_view(), name="producto_list"),
    path('productos/<int:pk>/', login_required(ProductoDetailView.as_view()), name="producto_detail"),
    path('productos/add/', user_passes_test(admin_required)(ProductoCreateView.as_view()), name="producto_add"),
    path('productos/<int:pk>/edit/', user_passes_test(admin_required)(ProductoUpdateView.as_view()), name="producto_edit"),
    path('productos/<int:pk>/delete/', user_passes_test(admin_required)(ProductoDeleteView.as_view()), name="producto_delete"),
    path('laboratorios/', LaboratorioListView.as_view(), name="laboratorio_list"),
    path('laboratorios/<int:pk>/', login_required(LaboratorioDetailView.as_view()), name="laboratorio_detail"),
    path('laboratorios/add/', user_passes_test(admin_required)(LaboratorioCreateView.as_view()), name="laboratorio_add"),
    path('laboratorios/<int:pk>/edit/', user_passes_test(admin_required)(LaboratorioUpdateView.as_view()), name="laboratorio_edit"),
    path('laboratorios/<int:pk>/delete/', user_passes_test(admin_required)(LaboratorioDeleteView.as_view()), name="laboratorio_delete"),
    path('directores/', DirectorGeneralListView.as_view(), name="director_list"),
    path('directores/<int:pk>/', login_required(DirectorGeneralDetailView.as_view()), name="director_detail"),
    path('directores/add/', user_passes_test(admin_required)(DirectorGeneralCreateView.as_view()), name="director_add"),
    path('directores/<int:pk>/edit/', user_passes_test(admin_required)(DirectorGeneralUpdateView.as_view()), name="director_edit"),
    path('directores/<int:pk>/delete/', user_passes_test(admin_required)(DirectorGeneralDeleteView.as_view()), name="director_delete"),
]
