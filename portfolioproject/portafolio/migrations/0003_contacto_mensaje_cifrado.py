# Generated by Django 4.2.13 on 2024-07-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='mensaje_cifrado',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
