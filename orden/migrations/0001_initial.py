# Generated by Django 3.2.3 on 2022-05-15 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remedios', '0004_alter_remedios_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('monto_pago', models.IntegerField(blank=True, null=True)),
                ('mercadopago_token', models.CharField(max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='remedioOrdenado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField(default=1)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remedios', to='orden.orden')),
                ('remedio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remedios', to='remedios.remedios')),
            ],
        ),
    ]
