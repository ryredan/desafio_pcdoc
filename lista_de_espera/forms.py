from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    nome = forms.CharField(label='Nome: ', max_length=100)
    prioridade = forms.Select()

    class Meta:
        model = Paciente
        fields = '__all__'