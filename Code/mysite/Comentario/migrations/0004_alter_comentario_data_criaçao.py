# Generated by Django 4.0.3 on 2023-05-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comentario', '0003_comentario_data_criaçao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='Data_criaçao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
