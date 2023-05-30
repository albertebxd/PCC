from django import forms 
from .models import Comentario

class createForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields = ('Conteudo',)

class createForm2(forms.ModelForm):
    class Meta:
        model= Comentario
        fields = ('Conteudo', 'Livro_comentario')