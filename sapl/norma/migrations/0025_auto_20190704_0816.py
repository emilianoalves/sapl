# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-04 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0024_auto_20190425_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='normajuridica',
            name='apelido',
            field=models.TextField(blank=True, verbose_name='Apelido'),
        ),
        migrations.AddField(
            model_name='normajuridica',
            name='norma_de_destaque',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Norma de Destaque ?'),
        ),
    ]