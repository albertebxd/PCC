from django.db import models
from Perfil.models import Perfil

# Create your views here.
class Interaçao(models.Model):
    Data_inicio = models.DateField(auto_now_add = True)
    Seguidor = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='Seguidor')
    Pessoa_seguida = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='Pessoa_seguida')
