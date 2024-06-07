# Generated by Django 4.0.10 on 2024-06-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0006_rename_resenha_resegna_resegna_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='libro',
        ),
        migrations.AddField(
            model_name='libro',
            name='categorias',
            field=models.ManyToManyField(related_name='libros', to='libros.categoria'),
        ),
    ]