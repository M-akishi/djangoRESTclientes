from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Edad', 'Saldo', 'Activo', 'Nivel_de_Satisfaccion','Genero']