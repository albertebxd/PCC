from django.db import models

# Create your models here.
class Livro(models.Model):
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
    Imagem = models.ImageField(upload_to='static/imagens', null=True, blank=True)
    is_valid = models.BooleanField(default='False')
    #adicionar mais categorias depois 
    Quant_leituras = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.Titulo)