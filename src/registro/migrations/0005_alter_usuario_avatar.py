# Generated by Django 5.1.4 on 2024-12-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_alter_usuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/core/img/imagenes_perfil'),
        ),
    ]
