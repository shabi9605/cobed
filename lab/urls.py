from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('add_test/',views.add_test,name='add_test'),
    path('test_list/', views.test_list, name='test_list'),
    path('test_update/<int:id>/', views.test_update, name='test_update'),
    path('test_delete/<int:id>/', views.test_delete, name='test_delete'),

    path('lab_data/', views.lab_data, name='lab_data'),

    path('update_availbility/<int:id>/', views.update_availbility, name='update_availbility'),

    path('add_patient_lab/',views.add_patient_lab,name='add_patient_lab'),  
    path('lab_patient_view/',views.lab_patient_view,name='lab_patient_view'),
    path('update_patient_lab/<int:id>/',views.update_patient_lab,name='update_patient_lab'),
    path('delete_patient_lab/<int:id>/',views.delete_patient_lab,name='delete_patient_lab'),

    path('patient_status_list/',views.patient_status_list,name='patient_status_list'),
    path('update_patientstatus_lab/<int:id>/',views.update_patientstatus_lab,name='update_patientstatus_lab'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)