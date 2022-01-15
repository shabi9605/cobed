from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('view_patient/',views.view_patient,name='view_patient'),
    path('complaint/',views.complaint,name='complaint'),
    path('complaint_list/',views.complaint_view,name='complaint_list'),
    path('complaint_replay/<int:id>/',views.complaint_replay,name='complaint_replay'),
    path('complaint_replay_view/',views.complaint_replay_view,name='com_replay_view'),

    path('complaint_pass_dmo/<int:id>/',views.complaint_pass_dmo,name='complaint_pass_dmo'),

    path('chat/',views.chat,name='chat'),
    path('chat_replay_view/',views.chat_replay_view,name='chat_replay_view'),
    path('chat_view/',views.chat_view,name='chat_view'),
    path('chat_replay/<int:id>/',views.chat_replay,name='chat_replay'),
    path('dmo_complaint/',views.dmo_complaint,name='dmo_complaint'),


    path('dmo_view_complaint/',views.dmo_view_complaint,name='dmo_view_complaint'),

    path('home_view_complaint',views.home_view_complaint,name='home_view_complaint'),

    path('view_details',views.view_details,name='view_details'),

    path('view_all_patients',views.view_all_patients,name='view_all_patients'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)