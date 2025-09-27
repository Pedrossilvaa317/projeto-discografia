from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('disco/', include('disco.urls', namespace='disco')),
    path('admin/', admin.site.urls),
]

# --- Adicione esta linha no final do ficheiro ---
# Isto serve os ficheiros de media apenas em modo de desenvolvimento (DEBUG=True)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)