# Generated by Django 3.2.3 on 2022-05-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedios', '0003_alter_remedios_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remedios',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Miniatura de la imagen del remedio'),
        ),
    ]
