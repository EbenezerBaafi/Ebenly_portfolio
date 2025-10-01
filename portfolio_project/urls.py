from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # This now maps to the root URL (/)
    path('', include('Portfolio.urls')), 
]

# Ensure your media configuration is still included below
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)