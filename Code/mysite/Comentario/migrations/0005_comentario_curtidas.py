# Generated by Django 4.0.3 on 2023-05-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comentario', '0004_alter_comentario_data_criaçao'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='Curtidas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
