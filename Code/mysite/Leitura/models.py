from django.db import models
from Perfil.models import Perfil
from Livro.models import Livro

# Create your views here.
class Leitura(models.Model):
    STATUS = (
        ('Quero ler', 'Quero ler'),
        ('Lido', 'Lido'), 
        ('Lendo', 'Lendo')
    )
    AVALIAÇAO = (
        (1, 1),
        (2, 2),
        (3, 3), 
        (4, 4),
        (5, 5)
    )
    Data_inicio = models.DateField()
    Data_final = models.DateField()
    Avaliacao = models.IntegerField(choices=AVALIAÇAO)
    Status = models.CharField(max_length=1000, choices=STATUS)
    Leitor = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='Leitor')
    Livro_lido = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='Livro_lido')

    def __str__(self):
        return str(self.Livro_lido)