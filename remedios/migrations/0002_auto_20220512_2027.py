# Generated by Django 3.2.3 on 2022-05-12 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remedios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaRemedio',
            fields=[
                ('idMarcaRemedio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Marca del remedio')),
                ('nombreMarcaRemedio', models.CharField(max_length=50, verbose_name='Nombre de la marca del remedio')),
            ],
        ),
        migrations.AlterField(
            model_name='categoriaremedio',
            name='nombreCategoria',
            field=models.CharField(max_length=250, verbose_name='Nombre de la Categoria'),
        ),
        migrations.CreateModel(
            name='Remedios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('nombreRemedio', models.CharField(max_length=100, verbose_name='Nombre del remedio')),
                ('descripcionRemedio', models.CharField(max_length=500, verbose_name='Descripción del remedio')),
                ('precioRemedio', models.IntegerField(verbose_name='Precio del remedio')),
                ('stockRemedio', models.IntegerField(blank=True, null=True, verbose_name='Stock del remedio')),
                ('cantidadRemedio', models.CharField(max_length=15, verbose_name='Cantidad de remedio en gr o mg')),
                ('imagenRemedio', models.ImageField(upload_to='uploads/', verbose_name='Imagen del remedio')),
                ('thumbnail', models.ImageField(upload_to='uploads/', verbose_name='Miniatura de la imagen del remedio')),
                ('fechaAgregado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remedios', to='remedios.categoriaremedio')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remedios.marcaremedio')),
            ],
            options={
                'ordering': ('-fechaAgregado',),
            },
        ),
    ]