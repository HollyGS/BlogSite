from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('contact/contact/', include('contact.urls')),
    path('about/', include('about.urls')),
    path('tinymce/', include('tinymce.urls')),
]
