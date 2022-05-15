from io import BytesIO #Esto nos ayuda a manejar las imagenes y las redimensionar
from PIL import Image

from django.core.files import File #esto nos ayuda a crear thumbnails(miniaturas)
from django.db import models

# Create your models here.
class CategoriaRemedio(models.Model):
    nombreCategoria = models.CharField(max_length=250, verbose_name="Nombre de la Categoria")
    slug = models.SlugField()

    class Meta:
        ordering = ('nombreCategoria',)

    def __str__(self):
        return self.nombreCategoria
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


class MarcaRemedio(models.Model):
    idMarcaRemedio = models.IntegerField(primary_key=True, verbose_name="Marca del remedio")
    nombreMarcaRemedio = models.CharField(max_length=50, verbose_name="Nombre de la marca del remedio")

    def __str__(self):
        return self.nombreMarcaRemedio


class Remedios(models.Model):
    categoria = models.ForeignKey(CategoriaRemedio, related_name='remedios', on_delete=models.CASCADE)
    marca = models.ForeignKey(MarcaRemedio, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()
    nombreRemedio = models.CharField(max_length=100, verbose_name="Nombre del remedio")
    descripcionRemedio = models.CharField(max_length=500, verbose_name="Descripción del remedio")
    precioRemedio = models.IntegerField(verbose_name="Precio del remedio")
    stockRemedio = models.IntegerField(blank=True, null=True ,verbose_name="Stock del remedio")
    cantidadRemedio = models.CharField(max_length=15 ,verbose_name="Cantidad de remedio en gr o mg")
    imagenRemedio = models.ImageField(upload_to='uploads/', verbose_name="Imagen del remedio")
    thumbnail = models.ImageField(upload_to='uploads/', verbose_name="Miniatura de la imagen del remedio",blank=True, null=True)
    fechaAgregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fechaAgregado',)

    def __str__(self):
        return self.nombreRemedio
    
    def get_absolute_url(self):
        return f'/{self.categoria.slug}/{self.slug}/'

    def get_image(self): #esta funcion nos permite obtener la url de la imagen
        if self.imagenRemedio:
            return 'http://127.0.0.1:8000' + self.imagenRemedio.url
        return ''
    
    def get_thumbnail(self): #esta funcion nos permite obtener la url del thumbnail
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.imagenRemedio:
                self.thumbnail = self.make_thumbnail(self.imagenRemedio)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        imagen = Image.open(image)
        imagen.convert('RGB')
        imagen.thumbnail(size)

        thumb_io = BytesIO()
        imagen.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail