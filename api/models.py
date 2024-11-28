from django.db import models

# Create your models here.

class Cliente(models.Model):
    ESTADO_CHOICES = [
        (1, 'Activo'),
        (0, 'Inactivo'),
    ]
    NIVEL_SATISFACCION_CHOICES = [
        (0,'No informado'),
        (1, 'Muy Insatisfecho'),
        (2, 'Insatisfecho'),
        (3, 'Neutral'),
        (4, 'Satisfecho'),
        (5, 'Muy Satisfecho'),
    ]
    
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No informado'),
    ]
    Cliente_id = models.AutoField(primary_key=True)
    Edad = models.PositiveSmallIntegerField()
    Saldo = models.DecimalField(max_digits=10, decimal_places=2)
    Genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='M')
    Activo = models.IntegerField(choices=ESTADO_CHOICES, default=1)
    Nivel_de_Satisfaccion = models.IntegerField(choices=NIVEL_SATISFACCION_CHOICES, default=3)

    def __str__(self):
        return f"Cliente {self.Cliente_id} - Edad: {self.Edad} - Saldo: {self.Saldo} - Estado: {self.Activo} - Satisfacción: {self.Nivel_de_Satisfaccion}"
