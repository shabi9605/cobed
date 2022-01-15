from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('home_view_patients',views.view_patients,name='home_view_patients'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)