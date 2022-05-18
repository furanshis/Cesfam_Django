from django.urls import path
from .views import *

urlpatterns = [
    path('correo/', enviarCorreo),
]