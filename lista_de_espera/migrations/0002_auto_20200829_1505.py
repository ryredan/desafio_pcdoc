# Generated by Django 3.1 on 2020-08-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_de_espera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='prioridade',
            field=models.IntegerField(choices=[(0, 'Caso geral'), (1, 'Encaminhado pelo médico'), (2, 'Gestante'), (3, 'Idoso'), (4, 'PCD')]),
        ),
    ]
