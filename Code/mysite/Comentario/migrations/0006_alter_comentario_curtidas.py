# Generated by Django 4.0.3 on 2023-05-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comentario', '0005_comentario_curtidas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='Curtidas',
            field=models.IntegerField(default=0),
        ),
    ]