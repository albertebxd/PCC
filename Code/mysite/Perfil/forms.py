from django import forms 
from .models import Perfil
class createForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = ('Nome', 'Sobrenome', 'Email', 'Data_nascimento', 'Bio', 'Cidade', 'Estado', 'Genero', 'Telefone', 'Imagem' )

class updateForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = ('Nome', 'Sobrenome', 'Email', 'Bio', 'Cidade', 'Estado', 'Genero', 'Telefone')
