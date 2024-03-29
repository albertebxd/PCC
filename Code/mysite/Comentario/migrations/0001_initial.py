# Generated by Django 4.0.3 on 2023-05-26 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Livro', '0004_livro_is_valid'),
        ('Perfil', '0003_perfil_bio_perfil_cidade_perfil_estado_perfil_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Conteudo', models.TextField()),
                ('Autor_comentario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Autor_comentario', to='Perfil.perfil')),
                ('Livro_comentario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Livro_comentario', to='Livro.livro')),
            ],
        ),
    ]
