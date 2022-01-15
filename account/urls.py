from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard2/',views.dashboard2,name='dashboard2'),

   
    path('register/',views.register,name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('password/',views.change_password,name="change_password"),
    path('update_profile_center/',views.update_profile_center,name='update_profile_center'),
    
    path('patient_register/',views.patient_register,name='patient_register'),
    path('update_patient_register/',views.update_patient_register,name='update_patient_register'),
   
    path('doctor_register/',views.doctor_register,name='doctor_register'),
    path('update_doctor_profile/',views.update_doctor_register,name='update_doctor_profile'),

   
    path('home_register/',views.home_register,name='home_register'),
    path('update_home_register/',views.update_home_register,name='update_home_register'),
   
    path('user_register/',views.user_register,name='user_register'),
    path('update_user_register/',views.update_user_register,name='update_user_register'),

    path('lab_register/',views.lab_register,name='lab_register'),
    path('update_profile_lab/',views.update_profile_lab,name='update_profile_lab'),

    path('lab_register_hospital/',views.lab_register_hospital,name='lab_register_hospital'),

    path('dmo_register/',views.dmo_register,name='dmo_register'),
    path('update_dmo_register/',views.update_dmo_register,name='update_dmo_register'),

    path('update_dmo_register/',views.update_dmo_register,name='update_dmo_register'),

    path('allcenters/',views.allcenters,name='allcenters'),
    path('centerappruval/<int:id>/',views.centerappruval,name='centerappruval'),

    
    path('all_labs/',views.all_labs,name='all_labs'),
    path('labappruval/<int:id>/',views.labappruval,name='labappruval'),

    path('all_home/',views.all_home,name='all_home'),
    path('homeappruval/<int:id>/',views.homeappruval,name='homeappruval'),

       
    path('all_doctor/',views.all_doctor,name='all_doctor'),
    path('doctorappruval/<int:id>/',views.doctorappruval,name='doctorappruval'),

    path('all_dmo/',views.all_dmo,name='all_dmo'),
    path('dmoappruval/<int:id>/',views.dmoappruval,name='dmoappruval'),

    path('resultlabs/',views.resultlabs,name='resultlabs'),
    path('centerresult/',views.centerresult,name='centerresult'),
    path('homeresult/',views.homeresult,name='homeresult'),
    path('search_hospital/',views.search_hospital,name='search_hospital'),

    path('search_pincode/',views.search_pincode,name='search_pincode'),



    path('hospital_search/',views.hospital_search,name='hospital_search'),
    path('inproper_death',views.inproper_death,name='inproper_death'),

    path('domicile_search',views.domicile_search,name='domicile_search'),
    path('csltc_search',views.csltc_search,name='csltc_search'),
    path('cfltc_search',views.cfltc_search,name='cfltc_search'),

    path('search_home',views.search_home,name='search_home'),

    path('map_view',views.map_view,name='map_view'),

    path('search_lab',views.search_lab,name='search_lab'),

    path('view_labs',views.view_labs,name='view_labs'),
    path('approve_lab/<int:id>/',views.approve_lab,name='approve_lab'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)