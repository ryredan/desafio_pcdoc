from django.db import models

class Paciente(models.Model):
    TIPO_PRIORIDADE = [
        (0, 'Caso geral'),
        (1, 'Encaminhado(a) pelo médico'),
        (2, 'Gestante'),
        (3, 'Idoso(a)'),
        (4, 'PCD')
        
    ]
    nome = models.CharField(max_length=100)
    prioridade = models.IntegerField(choices=TIPO_PRIORIDADE)

