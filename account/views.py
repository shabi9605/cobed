
from django.shortcuts import render,redirect
from patient.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
import random
import string
from django.core.mail import send_mail
from doctor.models import *
from home.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        Contacts.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return render(request,'contact.html',{'msg': 'Successfully sent message'})
    return render(request,'contact.html')

def centerresult(request):  
    today=datetime.now()

    
    center_patient_positive=PatientStatus.objects.filter(center=request.user.center,patient_status='positive').count()
    print(center_patient_positive)
    center_patient_negative=PatientStatus.objects.filter(center=request.user.center,patient_status='negative').count()
    print(center_patient_negative)
    center_patient_daeath=Death.objects.filter(user__center=request.user.center).count()
    patient_status=PatientStatus.objects.filter(patient_status='discharged')

    center_patient_positive_t=PatientStatus.objects.filter(center=request.user.center,patient_status='positive',created_date=today).count()
    center_patient_negative_t=PatientStatus.objects.filter(center=request.user.center,patient_status='negative',created_date=today).count()
    center_patient_daeath_t=Death.objects.filter(user__center=request.user.center,death_date=today).count()
    patient_status_t=PatientStatus.objects.filter(patient_status='discharged',created_date=today)

    doctors=Doctor.objects.filter(center=request.user.center,doctor_avilability='available').count()
    doctor=Doctor.objects.filter(center=request.user.center,doctor_avilability='available')

    

    context1={
            'center_patient_positive':center_patient_positive,
            'center_patient_negative':center_patient_negative,
            'center_patient_daeath':center_patient_daeath,
            'patient_status':patient_status,
            'doctors':doctors,
            'doctor':doctor,

            'center_patient_positive_t':center_patient_positive_t,
            'center_patient_negative_t':center_patient_negative_t,
            'center_patient_daeath_t':center_patient_daeath_t,
            'patient_status_t':patient_status_t
            }
    return render(request,'result/center.html',context1)


def homeresult(request):  
    today=datetime.now()

    
    center_patient_positive=PatientStatus.objects.filter(user=request.user,patient_status='positive').count()
    print(center_patient_positive)
    center_patient_negative=PatientStatus.objects.filter(user=request.user,patient_status='negative').count()
    print(center_patient_negative)
    center_patient_daeath=Death.objects.filter(user=request.user).count()
    patient_status=PatientStatus.objects.filter(patient_status='discharged')

    center_patient_positive_t=PatientStatus.objects.filter(user=request.user,patient_status='positive',created_date=today).count()
    center_patient_negative_t=PatientStatus.objects.filter(user=request.user,patient_status='negative',created_date=today).count()
    center_patient_daeath_t=Death.objects.filter(user=request.user,death_date=today).count()
    patient_status_t=PatientStatus.objects.filter(patient_status='discharged',created_date=today)

    # doctors=Doctor.objects.filter(center=request.user.center,doctor_avilability='available').count()
    # doctor=Doctor.objects.filter(center=request.user.center,doctor_avilability='available')

    

    context1={
            'center_patient_positive':center_patient_positive,
            'center_patient_negative':center_patient_negative,
            'center_patient_daeath':center_patient_daeath,
            'patient_status':patient_status,
            # 'doctors':doctors,
            # 'doctor':doctor,

            'center_patient_positive_t':center_patient_positive_t,
            'center_patient_negative_t':center_patient_negative_t,
            'center_patient_daeath_t':center_patient_daeath_t,
            'patient_status_t':patient_status_t
            }
    return render(request,'result/home.html',context1)


def resultlabs(request):  
    today=datetime.now()
    total_postive=Patient.objects.filter(patient_status='positive',user=request.user).count()
    total_negative=Patient.objects.filter(patient_status='negative',user=request.user).count()
    total_p=Patient.objects.filter(user=request.user).count()

    p_female=Patient.objects.filter(gender='Female',patient_status='positive',user=request.user).count()
    n_female=Patient.objects.filter(gender='Female',patient_status='negative',user=request.user).count()
    n_male=Patient.objects.filter(gender='Male',patient_status='negative',user=request.user).count()
    p_male=Patient.objects.filter(gender='Male',patient_status='positive',user=request.user).count()
    dm_total=Patient.objects.filter(gender='Male',user=request.user).count()
    df_total=Patient.objects.filter(gender='Female',user=request.user).count()

    tp_female=Patient.objects.filter(gender='Female',patient_status='positive',test_date=today,user=request.user).count()
    tn_female=Patient.objects.filter(gender='Female',patient_status='negative',test_date=today,user=request.user).count()
    tn_male=Patient.objects.filter(gender='Male',patient_status='negative',test_date=today,user=request.user).count()
    tp_male=Patient.objects.filter(gender='Male',patient_status='positive',test_date=today,user=request.user).count()
    tdm_total=Patient.objects.filter(gender='Male',user=request.user,created_date=today).count()
    tdf_total=Patient.objects.filter(gender='Female',user=request.user,created_date=today).count()

    total_postive_today=Patient.objects.filter(patient_status='positive',test_date=today,user=request.user).count()
    total_negative_today=Patient.objects.filter(patient_status='negative',test_date=today,user=request.user).count()
    total_today=Patient.objects.filter(created_date=today,user=request.user).count()
    
    # doctors=Doctor.objects.filter(user=request.user,doctor_avilability=available)

    context = {
            'total_postive':total_postive,
            'total_negative':total_negative,
            'total_p':total_p,
            'total_postive_today':total_postive_today,
            'total_negative_today':total_negative_today,
            'total_today':total_today,
             

            'p_female':p_female,
            'p_male':p_male,
            'n_female':n_female,
            'n_male':n_male, 
            'dm_total':dm_total,
            'df_total':df_total,

            'tp_female':tp_female,
            'tp_male':tp_male,
            'tn_female':tn_female,
            'tn_male':tn_male, 
            'tdm_total':tdm_total,
            'tdf_total':tdf_total
            
            }
    return render(request,'result/result1.html',context)



def dashboard(request):
    today=datetime.now()
    total_postive=PatientStatus.objects.filter(patient_status='positive').count()
    total_negative=PatientStatus.objects.filter(patient_status='negative').count()
    total_deathcase=Death.objects.all().count()

    p_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive').count()
    n_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='negative').count()
    n_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='negative').count()
    p_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive').count()
    dm_death=Death.objects.filter(patient__gender='Male').count()
    df_death=Death.objects.filter(patient__gender='Female').count()

    tp_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',created_date=today).count()
    tn_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='negative',created_date=today).count()
    tn_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='negative',created_date=today).count()
    tp_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',created_date=today).count()
    tdm_death=Death.objects.filter(patient__gender='Male',death_date=today).count()
    tdf_death=Death.objects.filter(patient__gender='Female',death_date=today).count()

    total_postive_today=PatientStatus.objects.filter(patient_status='positive',created_date=today).count()
    total_negative_today=PatientStatus.objects.filter(patient_status='negative',created_date=today).count()
    total_deathcase_today=Death.objects.filter(death_date=today).count()
    
    doctors=Doctor.objects.filter(user=request.user,doctor_avilability=available)

    context = {
            'total_postive':total_postive,
            'total_negative':total_negative,
            'total_deathcase':total_deathcase,
            'total_postive_today':total_postive_today,
            'total_negative_today':total_negative_today,
            'total_deathcase_today':total_deathcase_today,
            'doctors':doctors, 

            'p_female':p_female,
            'p_male':p_male,
            'n_female':n_female,
            'n_male':n_male, 
            'dm_death':dm_death,
            'df_death':df_death,

            'tp_female':tp_female,
            'tp_male':tp_male,
            'tn_female':tn_female,
            'tn_male':tn_male, 
            'tdm_death':tdm_death,
            'tdf_death':tdf_death
            
            }
    
    return render(request,'dashboard/index.html',context)

def dashboard2(request):
    return render(request,'dashboard/center.html')

def register(request):
    if request.method=='POST':
        user_form=UserForm(request.POST)              
        profile_form=ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')

            center_name=request.POST.get('center_name')
            authority_type=request.POST.get('authority_type')
            center_pincode=request.POST.get('center_pincode')
            center_place=request.POST.get('center_place')
            center_type=request.POST.get('center_type')
            center_phone=request.POST.get('center_phone')
            center_ideantification_proof=request.FILES.get('center_ideantification_proof')
            center_photo=request.FILES.get('center_photo')

            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            # usernew.save()
            profile=Center.objects.create(
                user=usernew,
               
                center_name=center_name,
                authority_type=authority_type,
                center_pincode=center_pincode,
                center_place=center_place,
                center_type=center_type,
                center_phone=center_phone,
                center_ideantification_proof=center_ideantification_proof,
                center_photo=center_photo



            )
            profile.save()
          
         
            # send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])

            messages.success(request,'Thank You For Registering')
            return redirect('signin')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
       
    return render(request,'account/center_register.html',{'user_form':user_form,'profile_form':profile_form})

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(list)
        try:
            user1=Center.objects.get(user=user)
           
        except:
            pass
        if user:
            if user.is_active:
                try:
                    if user1:
                        active=Center.objects.all().filter(user_id=user.id,status_appruval=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            # return HttpResponse("Waiting for approval")
                            messages.success(request,'waiting for approval')
                            return redirect('signin')
                    
                except:
                    pass
                try:
                    if Lab.objects.get(user=user):
                        active=Lab.objects.all().filter(user_id=user.id,status_appruval=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            # return HttpResponse("Waiting for approval")
                            messages.success(request,'waiting for approval')
                            return redirect('signin')
                    
                except:
                    pass
                
                try:
                    if Home.objects.get(user=user):
                        active=Home.objects.all().filter(user_id=user.id,status_appruval=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            # return HttpResponse("Waiting for approval")
                            messages.success(request,'waiting for approval')
                            return redirect('signin')
                    
                except:
                    pass              

                try:
                    if DMO.objects.get(user=user):
                        active=DMO.objects.all().filter(user_id=user.id,status_appruval=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            # return HttpResponse("Waiting for approval")
                            messages.success(request,'waiting for approval')
                            return redirect('signin')
                    
                except:
                    pass              
             
             
                try:   
                    login(request,user)            
                    return HttpResponseRedirect(reverse('dashboard'))
                    
                except:
                    pass

                try:
                    if user.is_superuser:
                        
                        login(request,user)
                
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        messages.success(request,'waiting for approval')
                        return redirect('signin')
                        # return HttpResponse("Waiting for approval")
                except:
                    pass
            else:
                return HttpResponse("Not active")       
        else:
            # return HttpResponse("Invalid username or password")
            messages.error(request,'Invalid username or password')
            return redirect('signin')
    else:
        return render(request,'account/login.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCEFULLY UPDATED")
            return render(request,'account/change_password.html')
        else:
            messages.error(request,'PLEASE CORRECT ERROR')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'account/change_password.html',{'form':form})


def update_profile_center(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        
        update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.center)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user.center)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'account/update_profile.html',context)

def patient_register(request):
   
    if request.method=='POST':
        user_form=UserForm(request.POST)
        patient_form=Patient_RegisterForm(request.POST,request.FILES)

        if user_form.is_valid() and patient_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            # user=user_form.save()
            # user.save()

            profile=patient_form.save(commit=False)
            profile.user=usernew
            profile.save()
            send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])

            messages.success(request,'Thank You For Registering')
            return redirect('dashboard')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        patient_form=Patient_RegisterForm()
       
    return render(request,'account/patient_register.html',{'user_form':user_form,'patient_form':patient_form})


def update_patient_register(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_patient_form=UpdatePatientRegisterForm(request.POST,request.FILES,instance=request.user.patient_register)
        if update_form.is_valid() and update_patient_form.is_valid():
            update_form.save()
            update_patient_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_patient_form=UpdatePatientRegisterForm(instance=request.user.patient_register)

    context={
        'update_form':update_form,
        'update_patient_form':update_patient_form
    }
    return render(request,'account/update_patient_register.html',context)


def doctor_register(request):
    if request.method=='POST':
        user_form=UserForm(request.POST)
        doctor_form=Doctor_RegisterForm(request.POST,request.FILES)

        if user_form.is_valid() and doctor_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )

            profile=doctor_form.save(commit=False)
            profile.user=usernew
            profile.center=request.user.center
            profile.save()
            messages.success(request,'Thank You For Registering')
            return redirect('dashboard')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        doctor_form=Doctor_RegisterForm()
       
    return render(request,'account/doctor_register.html',{'user_form':user_form,'doctor_form':doctor_form})


def update_doctor_register(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_doctor_form=UpdateDoctorRegisterForm(request.POST,request.FILES,instance=request.user.doctor)
        if update_form.is_valid() and update_doctor_form.is_valid():
            update_form.save()
            update_doctor_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_doctor_form=UpdateDoctorRegisterForm(instance=request.user.doctor)

    context={
        'update_form':update_form,
        'update_doctor_form':update_doctor_form
    }
    return render(request,'account/update_doctor_register.html',context)



def home_register(request):
   
    if request.method=='POST':
        user_form=UserForm(request.POST)
        home_form=HomeForm(request.POST,request.FILES)

        if user_form.is_valid() and home_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            # user=user_form.save()
            # user.save()

            profile=home_form.save(commit=False)
            profile.user=usernew
            profile.save()
            send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])

            messages.success(request,'Thank You For Registering')
            return redirect('signin')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        home_form=HomeForm()
       
    return render(request,'account/home_register.html',{'user_form':user_form,'home_form':home_form})


def update_home_register(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_home_form=HomeProfileForm(request.POST,request.FILES,instance=request.user.home)
        if update_form.is_valid() and update_home_form.is_valid():
            update_form.save()
            update_home_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_home_form=HomeProfileForm(instance=request.user.home)

    context={
        'update_form':update_form,
        'update_home_form':update_home_form
    }
    return render(request,'account/update_home_register.html',context)



def user_register(request):
   
    if request.method=='POST':
        user_form=UserForm(request.POST)
        userregister_form=UserRegisterForm(request.POST,request.FILES)

        if user_form.is_valid() and userregister_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            # user=user_form.save()
            # user.save()

            profile=userregister_form.save(commit=False)
            profile.user=usernew
            profile.save()
            send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])

            messages.success(request,'Thank You For Registering')
            return redirect('signin')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        userregister_form=UserRegisterForm()
       
    return render(request,'account/user_register.html',{'user_form':user_form,'userregister_form':userregister_form})


def update_user_register(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_user_form=UpdateUserRegister(request.POST,request.FILES,instance=request.user.userregister)
        if update_form.is_valid() and update_user_form.is_valid():
            update_form.save()
            update_user_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_user_form=UpdateUserRegister(instance=request.user.userregister)

    context={
        'update_form':update_form,
        'update_user_form':update_user_form
    }
    return render(request,'account/update_user_register.html',context)


def lab_register(request):   
    if request.method=='POST':
        user_form=UserFormLab(request.POST)
        lab_form=ProfileFormLab(request.POST,request.FILES)

        if user_form.is_valid() and lab_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            

            profile=lab_form.save(commit=False)
            profile.user=usernew
            profile.save()
            send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])
            messages.success(request,'Thank You For Registering')
            return redirect('signin')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserFormLab()
        lab_form=ProfileFormLab()
       
    return render(request,'account/lab_register.html',{'user_form':user_form,'lab_form':lab_form})

def update_profile_lab(request):
    if request.method=="POST":
        update_form=UpdateFormLab(request.POST,instance=request.user)
        
        update_profile_form=LabUpdateForm(request.POST,request.FILES,instance=request.user.lab)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateFormLab(instance=request.user)
        update_profile_form=LabUpdateForm(instance=request.user.lab)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'account/update_profile_lab.html',context)



def dmo_register(request):
   
    if request.method=='POST':
        user_form=UserForm(request.POST)
        userregister_form=DmoForm(request.POST,request.FILES)

        if user_form.is_valid() and userregister_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            # user=user_form.save()
            # user.save()

            profile=userregister_form.save(commit=False)
            profile.user=usernew
            profile.save()
            send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])

            messages.success(request,'Thank You For Registering')
            return redirect('signin')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        userregister_form=DmoForm()
       
    return render(request,'account/dmo_register.html',{'user_form':user_form,'userregister_form':userregister_form})


def update_dmo_register(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_user_form=UpdateDmoForm(request.POST,request.FILES,instance=request.user.dmo)
        if update_form.is_valid() and update_user_form.is_valid():
            update_form.save()
            update_user_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_user_form=UpdateDmoForm(instance=request.user.userregister)

    context={
        'update_form':update_form,
        'update_user_form':update_user_form
    }
    return render(request,'account/update_dmo_register.html',context)


def lab_register_hospital(request):   
    if request.method=='POST':
        user_form=UserFormLab(request.POST)
        lab_form=LabFormHospital(request.POST,request.FILES)

        if user_form.is_valid() and lab_form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password1')
            p=password
            u=username
            usernew = User.objects.create_user(
                username=username,
                password=password,
            )
            

            profile=lab_form.save(commit=False)
            profile.user=usernew
            profile.save()
            # send_mail('Username:'+str(u),'Password:'+str(p),'shabi960580@gmail.com',[u])
            messages.success(request,'Thank You For Registering')
            return redirect('signin')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserFormLab()
        lab_form=LabFormHospital()
       
    return render(request,'account/hospital_lab_register.html',{'user_form':user_form,'lab_form':lab_form})


def allcenters(request):
    c=Center.objects.all()
    return render(request,'admin/centers.html',{'c':c})

def centerappruval(request,id):
    u=Center.objects.get(id=id)
    form=AdminCenterProfileForm(instance=u)
    if request.method=='POST':
        form=AdminCenterProfileForm(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully appruved')
            return redirect('dashboard')
       
    return render(request,'admin/centers_appruval.html',{'form':form})


def all_labs(request):
    c=Lab.objects.all()
    return render(request,'admin/labs.html',{'c':c})

def labappruval(request,id):
    u=Lab.objects.get(id=id)
    form=AdminLabProfileForm(instance=u)
    if request.method=='POST':
        form=AdminLabProfileForm(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully appruved')
            return redirect('dashboard')
    return render(request,'admin/lab_appruval.html',{'form':form,'u':u})

def all_home(request):
    c=Home.objects.all()
    return render(request,'admin/home.html',{'c':c})

def homeappruval(request,id):
    u=Home.objects.get(id=id)
    form=AdminHomeProfileForm(instance=u)
    if request.method=='POST':
        form=AdminHomeProfileForm(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully appruved')
            return redirect('dashboard')

    return render(request,'admin/home_appruval.html',{'form':form,'u':u})



def all_dmo(request):
    c=DMO.objects.all()
    return render(request,'admin/dmo.html',{'c':c})

def dmoappruval(request,id):
    u=DMO.objects.get(id=id)
    form=AdminDMOProfileForm(instance=u)
    if request.method=='POST':
        form=AdminDMOProfileForm(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully appruved')
            return redirect('dashboard')

       
    return render(request,'admin/dmo_appruval.html',{'form':form})



def all_doctor(request):
    c=Doctor.objects.all()
    return render(request,'admin/doctor.html',{'c':c})

def doctorappruval(request,id):
    u=Doctor.objects.get(id=id)
    form=AdminDoctorProfileForm(instance=u)
    if request.method=='POST':
        form=AdminDoctorProfileForm(request.POST,request.FILES,instance=u)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully appruved')
            return redirect('dashboard')
        
    return render(request,'admin/doctor_appruval.html',{'form':form})

def search_hospital(request):
    total_p=PatientStatus.objects.filter()
    return render(request,'result/search1.html')



def search_pincode(request):    
    if request.method=='GET':
        q=request.GET.get('query')
        lab_p=PatientStatus.objects.filter(center__center_name__icontains=q)|PatientStatus.objects.filter(center__center_pincode__icontains=q,)
        print(lab_p)
     
        # return render(request,'hos/patient_list.html',{'list':lab_p})
    return render(request,'result/search1.html',{'list':lab_p})





def hospital_search(request):
    hospitals=Center.objects.filter(center_type='Hospital')
    today=datetime.now()
    if request.method=="GET":
        hospital=request.GET.get('hospital')
        try:
            lab=Lab.objects.filter(center__center_name__icontains=hospital)
            print(lab)
            doctors=Doctor.objects.filter(center__center_name__icontains=hospital)
            print(doctors)
            total_beds=Bed.objects.filter(center__center_name__icontains=hospital).count()
            free_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='free').count()
            occupied_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='occupied').count()
            oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='yes').count()
            without_oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='no').count()
            ventilator_beds=Bed.objects.filter(center__center_name__icontains=hospital,ventilator_no__isnull=False).count() #.exclude(ventilator_no__isnull=True,icu_no__isnull=False,icu_no=None,ward_no__isnull=False,ward_no=None)
            print(ventilator_beds)
            ward_beds=Bed.objects.filter(center__center_name__icontains=hospital,ward_no__isnull=False).count()#.exclude(ventilator_no__isnull=False,ventilator_no=None,icu_no__isnull=False,icu_no=None,ward_no__isnull=True)
            icu_beds=Bed.objects.filter(center__center_name__icontains=hospital,icu_no__isnull=False).count() #.exclude(ventilator_no__isnull=False,ventilator_no=None,icu_no__isnull=True,ward_no__isnull=False,ward_no=None)
            room_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_no__isnull=False).count()
            print(ward_beds)
            print(total_beds)
            today_positive=PatientStatus.objects.filter(patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            today_negative=PatientStatus.objects.filter(patient_status='negative',created_date=today,center__center_name__icontains=hospital).count()
            today_death=Death.objects.filter(death_date=today,center__center_name__icontains=hospital).count()
            tp_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            tp_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()



            total_positive_cases=PatientStatus.objects.filter(patient_status='positive',center__center_name__icontains=hospital).count()
            total_negative_cases=PatientStatus.objects.filter(patient_status='negative',center__center_name__icontains=hospital).count()
            total_death=Death.objects.filter(center__center_name__icontains=hospital).count()
            total_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',center__center_name__icontains=hospital).count()
            total_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',center__center_name__icontains=hospital).count()




            dmo_view_patients=PatientStatus.objects.filter(center__center_name__icontains=hospital)
            print(dmo_view_patients)

            print(tp_male)

            
            hospitals=Center.objects.filter(center_type='Hospital')
            return render(request,'account/serach_hopital.html',{'lab':lab,'doctors':doctors,'total_beds':total_beds,'free_beds':free_beds,'occupied_beds':occupied_beds,'oxygen_beds':oxygen_beds,'without_oxygen_beds':without_oxygen_beds,'today_positive':today_positive,'today_negative':today_negative,'today_death':today_death,'tp_male':tp_male,'tp_female':tp_female,'total_positive_cases':total_positive_cases,'total_negative_cases':total_negative_cases,'total_death':total_death,'total_male':total_male,'total_female':total_female,'dmo_view_patients':dmo_view_patients,'hospitals':hospitals,'ventilator_beds':ventilator_beds,'ward_beds':ward_beds,'icu_beds':icu_beds,'room_beds':room_beds})
        except:
            pass
        
    return render(request,'account/serach_hopital.html',{'hospitals':hospitals})




def domicile_search(request):
    hospitals=Center.objects.filter(center_type='Domicile')
    today=datetime.now()
    if request.method=="GET":
        hospital=request.GET.get('hospital')
        try:
            lab=Lab.objects.filter(center__center_name__icontains=hospital)
            print(lab)
            doctors=Doctor.objects.filter(center__center_name__icontains=hospital)
            print(doctors)
            total_beds=Bed.objects.filter(center__center_name__icontains=hospital).count()
            free_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='free').count()
            occupied_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='occupied').count()
            oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='yes').count()
            without_oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='no').count()
            print(total_beds)
            today_positive=PatientStatus.objects.filter(patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            today_negative=PatientStatus.objects.filter(patient_status='negative',created_date=today,center__center_name__icontains=hospital).count()
            today_death=Death.objects.filter(death_date=today,center__center_name__icontains=hospital).count()
            tp_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            tp_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()



            total_positive_cases=PatientStatus.objects.filter(patient_status='positive',center__center_name__icontains=hospital).count()
            total_negative_cases=PatientStatus.objects.filter(patient_status='negative',center__center_name__icontains=hospital).count()
            total_death=Death.objects.filter(center__center_name__icontains=hospital).count()
            total_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',center__center_name__icontains=hospital).count()
            total_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',center__center_name__icontains=hospital).count()




            dmo_view_patients=PatientStatus.objects.filter(center__center_name__icontains=hospital)
            print(dmo_view_patients)

            print(tp_male)

            
            hospitals=Center.objects.filter(center_type='Domicle')
            return render(request,'account/serach_hopital.html',{'lab':lab,'doctors':doctors,'total_beds':total_beds,'free_beds':free_beds,'occupied_beds':occupied_beds,'oxygen_beds':oxygen_beds,'without_oxygen_beds':without_oxygen_beds,'today_positive':today_positive,'today_negative':today_negative,'today_death':today_death,'tp_male':tp_male,'tp_female':tp_female,'total_positive_cases':total_positive_cases,'total_negative_cases':total_negative_cases,'total_death':total_death,'total_male':total_male,'total_female':total_female,'dmo_view_patients':dmo_view_patients,'hospitals':hospitals})
        except:
            pass
        
    return render(request,'account/serach_hopital.html',{'hospitals':hospitals})




def csltc_search(request):
    hospitals=Center.objects.filter(center_type='CSLTC')
    today=datetime.now()
    if request.method=="GET":
        hospital=request.GET.get('hospital')
        try:
            lab=Lab.objects.filter(center__center_name__icontains=hospital)
            print(lab)
            doctors=Doctor.objects.filter(center__center_name__icontains=hospital)
            print(doctors)
            total_beds=Bed.objects.filter(center__center_name__icontains=hospital).count()
            free_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='free').count()
            occupied_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='occupied').count()
            oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='yes').count()
            without_oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='no').count()
            print(total_beds)
            today_positive=PatientStatus.objects.filter(patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            today_negative=PatientStatus.objects.filter(patient_status='negative',created_date=today,center__center_name__icontains=hospital).count()
            today_death=Death.objects.filter(death_date=today,center__center_name__icontains=hospital).count()
            tp_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            tp_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()



            total_positive_cases=PatientStatus.objects.filter(patient_status='positive',center__center_name__icontains=hospital).count()
            total_negative_cases=PatientStatus.objects.filter(patient_status='negative',center__center_name__icontains=hospital).count()
            total_death=Death.objects.filter(center__center_name__icontains=hospital).count()
            total_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',center__center_name__icontains=hospital).count()
            total_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',center__center_name__icontains=hospital).count()




            dmo_view_patients=PatientStatus.objects.filter(center__center_name__icontains=hospital)
            print(dmo_view_patients)

            print(tp_male)

            
            hospitals=Center.objects.filter(center_type='CSLTC')
            return render(request,'account/serach_hopital.html',{'lab':lab,'doctors':doctors,'total_beds':total_beds,'free_beds':free_beds,'occupied_beds':occupied_beds,'oxygen_beds':oxygen_beds,'without_oxygen_beds':without_oxygen_beds,'today_positive':today_positive,'today_negative':today_negative,'today_death':today_death,'tp_male':tp_male,'tp_female':tp_female,'total_positive_cases':total_positive_cases,'total_negative_cases':total_negative_cases,'total_death':total_death,'total_male':total_male,'total_female':total_female,'dmo_view_patients':dmo_view_patients,'hospitals':hospitals})
        except:
            pass
        
    return render(request,'account/serach_hopital.html',{'hospitals':hospitals})


def cfltc_search(request):
    hospitals=Center.objects.filter(center_type='CFLTC')
    today=datetime.now()
    if request.method=="GET":
        hospital=request.GET.get('hospital')
        try:
            lab=Lab.objects.filter(center__center_name__icontains=hospital)
            print(lab)
            doctors=Doctor.objects.filter(center__center_name__icontains=hospital)
            print(doctors)
            total_beds=Bed.objects.filter(center__center_name__icontains=hospital).count()
            free_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='free').count()
            occupied_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_availability='occupied').count()
            oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='yes').count()
            without_oxygen_beds=Bed.objects.filter(center__center_name__icontains=hospital,bed_with_oxygen='no').count()
            print(total_beds)
            today_positive=PatientStatus.objects.filter(patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            today_negative=PatientStatus.objects.filter(patient_status='negative',created_date=today,center__center_name__icontains=hospital).count()
            today_death=Death.objects.filter(death_date=today,center__center_name__icontains=hospital).count()
            tp_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()
            tp_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',created_date=today,center__center_name__icontains=hospital).count()



            total_positive_cases=PatientStatus.objects.filter(patient_status='positive',center__center_name__icontains=hospital).count()
            total_negative_cases=PatientStatus.objects.filter(patient_status='negative',center__center_name__icontains=hospital).count()
            total_death=Death.objects.filter(center__center_name__icontains=hospital).count()
            total_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',center__center_name__icontains=hospital).count()
            total_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',center__center_name__icontains=hospital).count()




            dmo_view_patients=PatientStatus.objects.filter(center__center_name__icontains=hospital)
            print(dmo_view_patients)

            print(tp_male)

            
            hospitals=Center.objects.filter(center_type='CSLTC')
            return render(request,'account/serach_hopital.html',{'lab':lab,'doctors':doctors,'total_beds':total_beds,'free_beds':free_beds,'occupied_beds':occupied_beds,'oxygen_beds':oxygen_beds,'without_oxygen_beds':without_oxygen_beds,'today_positive':today_positive,'today_negative':today_negative,'today_death':today_death,'tp_male':tp_male,'tp_female':tp_female,'total_positive_cases':total_positive_cases,'total_negative_cases':total_negative_cases,'total_death':total_death,'total_male':total_male,'total_female':total_female,'dmo_view_patients':dmo_view_patients,'hospitals':hospitals})
        except:
            pass
        
    return render(request,'account/serach_hopital.html',{'hospitals':hospitals})




def inproper_death(request):
    deaths=Death.objects.filter(appruval=False)
    return render(request,'account/inproper_deaths.html',{'deaths':deaths})



def search_home(request):
    home=Home.objects.all()
    today=datetime.now()
    print(today)
    if request.method=="GET":
        hospital=request.GET.get('hospital')
        try:
            
            today_positive=PatientStatus.objects.filter(patient_status='positive',created_date=today,home__name__icontains=hospital).count()
            print(today_positive)
            today_negative=PatientStatus.objects.filter(patient_status='negative',created_date=today,home__name__icontains=hospital).count()
            print(today_negative)
            
            tp_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',created_date=today,home__name__icontains=hospital).count()
            print(tp_male)
            tp_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',created_date=today,home__name__icontains=hospital).count()
            print(tp_female)



            total_positive_cases=PatientStatus.objects.filter(patient_status='positive',home__name__icontains=hospital).count()
            print(total_positive_cases)
            total_negative_cases=PatientStatus.objects.filter(patient_status='negative',home__name__icontains=hospital).count()
            print(total_negative_cases)
           
            total_male=PatientStatus.objects.filter(patient__gender='Male',patient_status='positive',home__name__icontains=hospital).count()
            print(total_male)
            total_female=PatientStatus.objects.filter(patient__gender='Female',patient_status='positive',home__name__icontains=hospital).count()
            print(total_female)




            dmo_view_patients=PatientStatus.objects.filter(home__name__icontains=hospital)
            print(dmo_view_patients)

            

            
            home=Home.objects.all()
            return render(request,'account/serach_home.html',{'today_positive':today_positive,'today_negative':today_negative,
            'tp_male':tp_male,'tp_female':tp_female,'total_positive_cases':total_positive_cases,
            'total_negative_cases':total_negative_cases,'total_male':total_male,
            'total_female':total_female,'dmo_view_patients':dmo_view_patients,'home':home})
        except:
            pass
        
    return render(request,'account/serach_home.html',{'home':home})






def map_view(request):
    return render(request,'account/map_view.html')




def search_lab(request):
    labs=Lab.objects.all()
    today=datetime.now()
    print(today)
    if request.method=="GET":
        hospital=request.GET.get('hospital')
        try:
            lab=Lab.objects.get(lab_name__icontains=hospital)
            print(lab)
            test=Test.objects.filter(lab__lab_name__icontains=hospital)
            print(test)

            
            
            

        
            labs=Lab.objects.all()
            return render(request,'account/serach_lab.html',{'labs':labs,'lab':lab,'test':test})
        except:
            pass
        
    return render(request,'account/serach_lab.html',{'labs':labs})





def view_labs(request):
    labs=Lab.objects.filter(center=request.user.center)
    print(labs)
    return render(request,'hospital/view_labs.html',{'labs':labs})



def approve_lab(request,id):
    lab = Lab.objects.get(id=id)
    print(lab)
    form= AdminLabProfileForm(instance=lab)
    if request.method=='POST':
        form= AdminLabProfileForm(request.POST,request.FILES,instance=lab)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'lab/approve_lab.html',{'form':form})