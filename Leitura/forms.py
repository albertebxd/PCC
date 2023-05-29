from django import forms 
from .models import Leitura

class createForm(forms.ModelForm):
    class Meta:
        model= Leitura
        fields = ('Status', 'Data_inicio', 'Data_final', 'Avaliacao')
