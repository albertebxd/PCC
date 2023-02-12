from django import forms 
from .models import Perfil
class createForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = ('Nome', 'Sobrenome', 'Email', 'Data_nascimento', )
