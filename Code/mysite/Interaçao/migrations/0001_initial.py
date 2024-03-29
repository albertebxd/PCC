# Generated by Django 4.0.3 on 2023-05-29 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Perfil', '0003_perfil_bio_perfil_cidade_perfil_estado_perfil_genero_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_inicio', models.DateField(auto_now_add=True)),
                ('Pessoa_seguida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Pessoa_seguida', to='Perfil.perfil')),
                ('Seguidor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Seguidor', to='Perfil.perfil')),
            ],
        ),
    ]
