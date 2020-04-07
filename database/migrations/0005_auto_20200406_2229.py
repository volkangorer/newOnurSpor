# Generated by Django 2.0.3 on 2020-04-06 19:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20200406_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeri',
            name='galeri_content2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Video Ekleyin'),
        ),
        migrations.AlterField(
            model_name='club_information',
            name='club_content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='galeri',
            name='galeri_content',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf Ekleyin'),
        ),
    ]
