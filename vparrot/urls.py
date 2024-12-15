from django.contrib import admin
from django.urls import path
from backoffice.views import *
from django.conf import settings



urlpatterns = [
    path('', index, name='index'),    
    path('admin/', admin.site.urls),
    path('vehicules', vehicules, name='vehicules'),
    path('vehicule/<str:slug>/', details_vehicule, name='vehicule'),
    path('avis', avis, name='avis'),
    path('filter_cars/', filter_cars, name='filter_cars'),
    path('mentions_legales', mentions_legales, name='mentions_legales'),
    path('politique_confidentialite', politique_confidentialite, name='politique_confidentialite'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

