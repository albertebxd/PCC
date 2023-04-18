# Generated by Django 4.0.3 on 2023-02-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=1000)),
                ('Editora', models.CharField(max_length=1000)),
                ('Autor', models.CharField(max_length=1000)),
                ('Ano_lancamento', models.CharField(max_length=4)),
                ('Paginas', models.CharField(max_length=10)),
                ('ISBN', models.CharField(max_length=13)),
                ('Categoria', models.CharField(choices=[('Fantasia', 'Fantasia'), ('Romance', 'Romance'), ('Suspense', 'Suspense'), ('Contos', 'Contos')], max_length=100)),
            ],
        ),
    ]
