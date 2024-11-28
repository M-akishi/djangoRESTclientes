# Generated by Django 5.1.3 on 2024-11-27 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cliente_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1),
        ),
    ]
