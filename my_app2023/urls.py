from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_app2023 import settings
from app1.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)