# Generated by Django 4.0.3 on 2023-05-29 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leitura', '0003_leitura_favorito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leitura',
            name='Favorito',
        ),
    ]
