from django import forms 
from .models import Livro

class createForm(forms.ModelForm):
    class Meta:
        model= Livro
        fields = ('Titulo', 'Editora', 'Autor', 'Ano_lancamento', 'Paginas', 'ISBN', 'Categoria', 'Imagem')
