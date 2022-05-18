from django.urls import path

from orden import views

urlpatterns = [
    path('cobro/', views.pago),
]