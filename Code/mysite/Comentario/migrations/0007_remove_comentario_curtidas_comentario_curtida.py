# Generated by Django 4.0.3 on 2023-05-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0003_perfil_bio_perfil_cidade_perfil_estado_perfil_genero_and_more'),
        ('Comentario', '0006_alter_comentario_curtidas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='Curtidas',
        ),
        migrations.AddField(
            model_name='comentario',
            name='Curtida',
            field=models.ManyToManyField(related_name='Curtida', to='Perfil.perfil'),
        ),
    ]
