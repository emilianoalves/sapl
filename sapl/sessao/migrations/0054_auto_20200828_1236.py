# Generated by Django 2.2.13 on 2020-08-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0071_auto_20200609_1503'),
        ('sessao', '0053_auto_20200609_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedientemateria',
            name='situacao_pauta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='materia.Tramitacao', verbose_name='Situação Pauta'),
        ),
        migrations.AddField(
            model_name='ordemdia',
            name='situacao_pauta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='materia.Tramitacao', verbose_name='Situação Pauta'),
        ),
    ]
