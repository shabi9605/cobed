from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('patient_death/',views.patient_death,name='patient_death'),
    path('update_death/<int:id>/',views.update_death,name='update_death'),
    path('death_details/',views.death_details,name='death_details'),
    path('death_home/',views.death_home,name='death_home'),

    path('view_deaths',views.view_deaths,name='view_deaths'),
    path('approved_deaths',views.approved_deaths,name='approved_deaths'),

    path('chat',views.chat,name='chat'),
    path('view_my_chat',views.view_my_chat,name='view_my_chat'),
    path('patient_chat',views.patient_chat,name='patient_chat'),
    path('view_patient_chat',views.view_patient_chat,name='view_patient_chat'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)