from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls.static import serve as serve_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls')),
    path('robots.txt', serve_static, {'path': 'robots.txt'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)