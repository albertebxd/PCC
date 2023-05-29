from django import forms 
from .models import Comentario

class createForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields = ('Conteudo',)
