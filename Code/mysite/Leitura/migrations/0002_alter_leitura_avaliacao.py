# Generated by Django 4.0.3 on 2023-04-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leitura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitura',
            name='Avaliacao',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]