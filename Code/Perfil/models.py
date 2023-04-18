from django.db import models
from django.contrib.auth import get_user_model

class Perfil(models.Model):
    # Imagem de perfil 
    Nome = models.CharField(max_length=1000)
    Sobrenome = models.CharField(max_length=1000)
    Email = models.EmailField(max_length=256)
    Data_nascimento = models.DateField()
    Usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

