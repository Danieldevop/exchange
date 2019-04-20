from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from website import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
