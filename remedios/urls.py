from django.urls import path, include

from remedios import views

urlpatterns = [
    path('latest-remedios/', views.LatestRemediosList.as_view()),
    path('remedios/search/', views.search),
    path('remedios/<slug:categoria_slug>/<remedio_slug>/', views.RemediosDetail.as_view()),
    path('remedios/<slug:categoria_slug>/', views.CategoriaDetail.as_view()),
]