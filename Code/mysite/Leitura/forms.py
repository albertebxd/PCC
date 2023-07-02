from django import forms 
from .models import Leitura

class createForm(forms.ModelForm):
    class Meta:
        model= Leitura
        fields = ('Status', 'Data_inicio', 'Data_final', 'Avaliacao')

class editarForm(forms.ModelForm):
    class Meta:
        model= Leitura
        fields = ('Status', 'Data_final', 'Avaliacao', 'Meta_leitura', 'Data_inicio')

class createForm_meta(forms.ModelForm):
    class Meta:
        model= Leitura
        fields = ('Meta_leitura',)
