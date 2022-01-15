from os import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('search_patients/',views.search_patients,name='search_patients'),  
    path('patient_list/',views.patient_list,name='patient_list'),
    path('update_patientstatus_hos/<int:id>/',views.update_patientstatus_hos,name='update_patientstatus_hos'),

    path('add_bed/',views.add_bed,name='add_bed'),
    path('add_bed1/',views.add_bed1,name='add_bed1'),
    path('add_bed2/',views.add_bed2,name='add_bed2'),
    path('add_bed3/',views.add_bed3,name='add_bed3'),
    path('all_bed/',views.center_bed_list,name='all_bed'),

    path('center_patient/',views.center_patient,name='center_patient'),
    path('bed_statusr/<int:id>/',views.bed_statusr,name='bed_statusr'),
    path('status/',views.status,name='status'),
    path('bed_statusr/',views.bed_statusr,name='bed_statusr'),
    
    path('hospital_patient/',views.hospital_patient,name='hospital_patient'),

    path('newpatient/',views.newpatient,name='newpatient'),
    path('newpatientcfltc/',views.newpatientcfltc,name='newpatientcfltc'),
    path('newpatientdom/',views.newpatientdom,name='newpatientdom'),
    path('newpatienthome/',views.newpatienthome,name='newpatienthome'),

    path('patient_disease/<int:id>/',views.patient_diesease,name='patient_disease'),

    path('add_vaccine/<int:id>',views.add_vaccine,name='add_vaccine'),
    path('center_vaccine_list/',views.center_vaccine_list,name='center_vaccine_list'),
    path('all_vaccine//',views.all_vaccine,name='all_vaccine'),
    path('update_vaccine/<int:id>/',views.update_vaccine,name='update_vaccine'),

    path('patientshome/',views.patientshome,name='patientshome'),
    path('centerpatients/',views.centerpatients,name='centerpatients'),

    path('view_patients',views.view_patients,name='view_patients'),

    path('view_hospital_doctors',views.view_hospital_doctors,name='view_hospital_doctors'),

    path('covid_disese/<int:id>',views.covid_disese,name='covid_disese'),


   












]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)