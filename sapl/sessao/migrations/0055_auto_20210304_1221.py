# Generated by Django 2.2.13 on 2021-03-04 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0054_auto_20201013_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bancada',
            options={'ordering': ('-legislatura__numero', 'nome'), 'verbose_name': 'Bancada Parlamentar', 'verbose_name_plural': 'Bancadas Parlamentares'},
        ),
    ]