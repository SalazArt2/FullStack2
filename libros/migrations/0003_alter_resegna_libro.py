# Generated by Django 4.0.10 on 2024-06-06 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_resegna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resegna',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resegnas', to='libros.libro'),
        ),
    ]