# Generated by Django 4.0.3 on 2023-02-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Livro', '0001_initial'),
        ('Perfil', '0002_alter_perfil_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_inicio', models.DateField()),
                ('Data_final', models.DateField()),
                ('Avaliacao', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('Status', models.CharField(choices=[('Quero ler', 'Quero ler'), ('Lido', 'Lido'), ('Lendo', 'Lendo')], max_length=1000)),
                ('Leitor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Leitor', to='Perfil.perfil')),
                ('Livro_lido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Livro_lido', to='Livro.livro')),
            ],
        ),
    ]
