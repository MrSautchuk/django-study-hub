from django.db import models

class Quarto(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=80)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'Quarto {self.numero} — {self.tipo}'
