# Generated by Django 4.0.10 on 2024-06-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='licor',
            options={'permissions': [('special_status', 'Puede ver todos los licores')]},
        ),
        migrations.AlterField(
            model_name='licor',
            name='categorias',
            field=models.ManyToManyField(related_name='licores', to='licores.categoria'),
        ),
    ]
