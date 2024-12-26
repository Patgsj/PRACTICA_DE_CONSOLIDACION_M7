from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Producto, Laboratorio, DirectorGeneral
from .forms import DirectorGeneralForm

def admin_required(user):
    return user.is_staff

@login_required
def index(request):
    context = {
        'total_laboratorios': Laboratorio.objects.count(),
        'total_directores': DirectorGeneral.objects.count(),
        'total_productos': Producto.objects.count(),
    }
    return render(request, "laboratorio/index.html", context)

class ProductoListView(ListView):
    model = Producto
    template_name = "laboratorio/producto_list.html"
    context_object_name = "productos"
    paginate_by = 5

@method_decorator([login_required], name='dispatch')
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "laboratorio/producto_detail.html"
    context_object_name = "producto"

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    template_name = "laboratorio/producto_form.html"
    fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    success_url = reverse_lazy("laboratorio:producto_list")

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "laboratorio/producto_form.html"
    fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
    success_url = reverse_lazy("laboratorio:producto_list")

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "laboratorio/producto_confirm_delete.html"
    success_url = reverse_lazy("laboratorio:producto_list")

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = "laboratorio/laboratorio_list.html"
    context_object_name = "laboratorios"
    paginate_by = 5

@method_decorator([login_required], name='dispatch')
class LaboratorioDetailView(DetailView):
    model = Laboratorio
    template_name = "laboratorio/laboratorio_detail.html"
    context_object_name = "laboratorio"

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class LaboratorioCreateView(CreateView):
    model = Laboratorio
    template_name = "laboratorio/laboratorio_form.html"
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy("laboratorio:laboratorio_list")

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    template_name = "laboratorio/laboratorio_form.html"
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy("laboratorio:laboratorio_list")

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = "laboratorio/laboratorio_confirm_delete.html"
    success_url = reverse_lazy("laboratorio:laboratorio_list")

class DirectorGeneralListView(ListView):
    model = DirectorGeneral
    template_name = "laboratorio/director_list.html"
    context_object_name = "directores"
    paginate_by = 5

@method_decorator([login_required], name='dispatch')
class DirectorGeneralDetailView(DetailView):
    model = DirectorGeneral
    template_name = "laboratorio/director_detail.html"
    context_object_name = "director"

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class DirectorGeneralCreateView(CreateView):
    model = DirectorGeneral
    form_class = DirectorGeneralForm
    template_name = "laboratorio/director_form.html"
    success_url = reverse_lazy("laboratorio:director_list")

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class DirectorGeneralUpdateView(UpdateView):
    model = DirectorGeneral
    template_name = "laboratorio/director_form.html"
    fields = ['nombre', 'especialidad', 'laboratorio']
    success_url = reverse_lazy("laboratorio:director_list")

@method_decorator([login_required, user_passes_test(admin_required)], name='dispatch')
class DirectorGeneralDeleteView(DeleteView):
    model = DirectorGeneral
    template_name = "laboratorio/director_confirm_delete.html"
    success_url = reverse_lazy("laboratorio:director_list")
