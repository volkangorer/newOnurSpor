# Generated by Django 2.0.3 on 2020-04-06 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0003_club_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hakkimizda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', models.CharField(max_length=2000, verbose_name='İçerik')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.AlterField(
            model_name='club_information',
            name='club_content',
            field=models.CharField(max_length=2000, verbose_name='İçerik'),
        ),
    ]
