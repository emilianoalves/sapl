# Generated by Django 2.2.13 on 2021-02-25 14:27

from django.db import migrations
import image_cropping.fields
import sapl.compilacao.models


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0016_auto_20201013_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='imagem',
            field=image_cropping.fields.ImageCropField(blank=True, null=True, upload_to=sapl.compilacao.models.imagem_upload_path, verbose_name='Imagem'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='imagem_cropping',
            field=image_cropping.fields.ImageRatioField('imagem', '0x0', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text='O recorte de imagem é possível após a atualização.', hide_image_field=False, size_warning=True, verbose_name='Recorte de Imagem'),
        ),
    ]