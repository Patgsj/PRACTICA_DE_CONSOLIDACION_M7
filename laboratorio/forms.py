from django import forms
from .models import DirectorGeneral, Laboratorio

class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = ['nombre', 'especialidad', 'laboratorio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del director'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la especialidad'}),
            'laboratorio': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['laboratorio'].queryset = Laboratorio.objects.filter(
            directorgeneral__isnull=True
        )
