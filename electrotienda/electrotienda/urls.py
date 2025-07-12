from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from productos import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria/', views.galeria_productos, name='galeria'),
    path('contacto/', views.contacto, name='contacto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)