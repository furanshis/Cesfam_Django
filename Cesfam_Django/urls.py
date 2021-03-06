from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('remedios.urls')),
    path('api/v1/', include('orden.urls')),
    path('api/v1/', include('correo.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
