# Generated by Django 4.0.3 on 2023-06-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leitura', '0004_remove_leitura_favorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitura',
            name='Data_final',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='leitura',
            name='Data_inicio',
            field=models.DateField(blank=True),
        ),
    ]
