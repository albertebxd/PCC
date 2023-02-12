from django.db import models

# Create your models here.
class Livro(models.Model):
    # Imagem da capa 
    Titulo = models.CharField(max_length=1000)
    Editora = models.CharField(max_length=1000)
    Autor = models.CharField(max_length=1000)
    Ano_lancamento = models.CharField(max_length=4)
    Paginas = models.CharField(max_length=10)
    ISBN = models.CharField(max_length=13)
    Categorias = (
        ('Fantasia', 'Fantasia'),
        ('Romance', 'Romance'),
        ('Suspense', 'Suspense'), 
        ('Contos', 'Contos'),
    )
    
    Categoria = models.CharField(max_length=100, choices=Categorias)
    #adicionar mais categorias depois 

