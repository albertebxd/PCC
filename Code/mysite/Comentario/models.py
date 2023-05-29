from django.db import models
from Perfil.models import Perfil
from Livro.models import Livro

# Create your models here.
class Comentario(models.Model):
    Conteudo = models.TextField()
    Autor_comentario = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='Autor_comentario')
    Livro_comentario = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='Livro_comentario')
    