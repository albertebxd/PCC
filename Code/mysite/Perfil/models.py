from django.db import models
from django.contrib.auth import get_user_model

class Perfil(models.Model):
    # Imagem de perfil, genero, telefone(op), cidade, bio
    Nome = models.CharField(max_length=1000)
    Sobrenome = models.CharField(max_length=1000)
    Email = models.EmailField(max_length=256)
    Telefone = models.CharField(max_length=14, null=True, blank=True )
    Cidade = models.CharField(max_length=300, null=True, blank=True )
    Estado = models.CharField(max_length=300, null=True, blank=True )
    Data_nascimento = models.DateField()
    Imagem = models.ImageField(upload_to='static/imagens/fotoUsuario', null=True, blank=True)
    Usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    Generos = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    Genero = models.CharField(max_length=100, choices=Generos)
    Bio = models.TextField(max_length=14, null=True, blank=True )
