"""
URL configuration for wildworldzoo project.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('animals/', include('animals.urls')),  # ✅ updated from 'movies/'
    path('accounts/', include('accounts.urls')),
    #path('cart/', include('cart.urls')),
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
