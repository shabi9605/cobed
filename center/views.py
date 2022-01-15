
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

def patient_list(request):
    p=Patient.objects.all()
    return render(request,'hos/patient_list.html',{'list':p})


def search_patients(request):    
    if request.method=='GET':
        q=request.GET.get('query')
        lab_p=PatientStatus.objects.filter(patient__name__icontains=q,user=request.user)|PatientStatus.objects.filter(patient__adhar__icontains=q,)
        print(lab_p)
        # return render(request,'hos/patient_list.html',{'list':lab_p})
    return render(request,'hos/patient_list.html',{'list':lab_p})




def update_patientstatus_hos(request,id):
    Update = PatientStatus.objects.get(id=id)
    print(Update)
    form= PatientFormHospital(instance=Update)
    if request.method=='POST':
        form= PatientFormHospital(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            p_form=form.save()    
            p_form.user=request.user
            p_form.center=request.user.center
            p_form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'hos/add_bed.html',{'form':form,'patient':Update})
    
def add_bed(request):
    if request.method=='POST':
        form=BedForm(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.center=request.user.center
            p_form.save()
            request.session['p_form']=p_form.id

            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=BedForm()
    return render(request,'bed/add_bed.html',{'form':form})

def add_bed1(request):
    if request.method=='POST':
        form=BedForm1(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.center=request.user.center
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=BedForm1()
    return render(request,'bed/add_bed.html',{'form':form})

def add_bed2(request):
    if request.method=='POST':
        form=BedForm2(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.center=request.user.center
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=BedForm2()
    return render(request,'bed/add_bed.html',{'form':form})

def add_bed3(request):
    if request.method=='POST':
        form=BedForm3(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.center=request.user.center
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=BedForm3()
    return render(request,'bed/add_bed.html',{'form':form})



# def all_bed(request):
#     all_b=Bed.objects.all()
#     return render(request,'bed/all_bed.html',{'all_b':all_b})


def center_bed_list(request):

    r=Bed.objects.filter(user=request.user,bed_availability=free,ward_no=None,icu_no=None,ventilator_no=None)
    w=Bed.objects.filter(user=request.user,bed_availability=free,room_no=None,icu_no=None,ventilator_no=None)
    i=Bed.objects.filter(user=request.user,bed_availability=free,room_no=None,ward_no=None,ventilator_no=None)
    v=Bed.objects.filter(user=request.user,bed_availability=free,room_no=None,icu_no=None,ward_no=None)

    return render(request,'bed/all_bed.html',{'r':r,'w':w,'i':i,'v':v})


def center_patient(request):
    c=PatientStatus.objects.filter(center=request.user.center)
    return render(request,'patient/center_patient.html',{'c':c})



# def bed_statusr(request,id):
#     Update = Bed.objects.get(id=id)
#     print(Update)
#     form= UpdateBedForm1(instance=Update)
#     if request.method=='POST':
#         form= UpdateBedForm1(request.POST,request.FILES,instance=Update)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Record Update succefully')
#             return redirect('dashboard')
#     return render(request,'bed/update_roomp.html',{'form':form,})


def status(request):
    p=PatientStatus.objects.filter(user=request.user)
    return render(request,'status/status.html',{'p':p})

def bed_statusr(request,id):
    Update = PatientStatus.objects.get(id=id)
    print(Update)
    form= UpdateBedForm1(instance=Update)
    if request.method=='POST':
        form= UpdateBedForm1(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            p=form.save()
          
            p.save()

            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'bed/update_roomp.html',{'form':form,})


def newpatient(request):
    r=Bed.objects.filter(user=request.user,bed_availability=free,ward_no=None,icu_no=None,ventilator_no=None)
    patient_list=[]
    included_patients=Patient.objects.all()
    for i in included_patients:
        #print(i.patient.id)
        patient_list.append(i.patient.id)
    patients=Patient_Register.objects.exclude(id__in=patient_list)
    #print(patients)
    if request.method=='POST':
        form1=NewPatient(request.POST)
        form2=NewBed(request.POST)
        patient=request.POST.get('patient')
        print(patient)
        if form1.is_valid() and form2.is_valid():
            patient_hos_id=request.POST.get('patient_hos_id')
            name=request.POST.get('name')
            adhar=request.POST.get('adhar')
            phone=request.POST.get('phone')
            gender=request.POST.get('gender')

            bed_no=request.POST.get('bed_no')
            ward_no=request.POST.get('ward_no')
            floor_no=request.POST.get('floor_no')
            patient=Patient_Register.objects.get(id=patient)
            print(patient)
            form1=Patient(user=request.user,center=request.user.center,patient=patient,patient_hos_id=form1.cleaned_data['patient_hos_id'],
            name=form1.cleaned_data['name'],adhar=form1.cleaned_data['adhar'],gender=form1.cleaned_data['gender'],phone=form1.cleaned_data['phone'],pincode=form1.cleaned_data['pincode'],
            patient_status=form1.cleaned_data['patient_status'])
            # form1.patient=patient
            # form1.center=request.user.center
            form1.save()
        
           
            s=PatientStatus.objects.create(
                user=request.user,
                center=request.user.center,
               
                patient=form1,
                patient_status=form1.patient_status,
                
                bed=form2.save()
                )
            
            s.save()
            return redirect('dashboard')
        else:
            HttpResponse('invalid')
    else:
        form1=NewPatient()
        form2=NewBed()
    return render(request,'new/patient.html',{'form1':form1,'form2':form2,'patients':patients})

def hospital_patient(request):
    h=PatientStatus.objects.filter(user=request.user)
    return render(request,'hos/all_patient.html',{'h':h})

# def update_patient_status(request):

def newpatientcfltc(request):
    # r=Bed.objects.filter(user=request.user,bed_availability=free,ward_no=None,icu_no=None,ventilator_no=None)
    patient_list=[]
    included_patients=Patient.objects.all()
    for i in included_patients:
        patient_list.append(i.patient.id)
    patients=Patient_Register.objects.exclude(id__in=patient_list)
    
    if request.method=='POST':
        form1=NewPatient(request.POST)
        form2=NewBedcfltc(request.POST)
        patient=request.POST.get('patient')
        print(patient)
        if form1.is_valid() and form2.is_valid():
            patient_hos_id=request.POST.get('patient_hos_id')
            name=request.POST.get('name')
            adhar=request.POST.get('adhar')
            phone=request.POST.get('phone')
            gender=request.POST.get('gender')

            bed_no=request.POST.get('bed_no')
            ward_no=request.POST.get('ward_no')
            floor_no=request.POST.get('floor_no')
            patient=Patient_Register.objects.get(id=patient)
            print(patient)
            form1=Patient(user=request.user,center=request.user.center,patient=patient,patient_hos_id=form1.cleaned_data['patient_hos_id'],
            name=form1.cleaned_data['name'],adhar=form1.cleaned_data['adhar'],gender=form1.cleaned_data['gender'],phone=form1.cleaned_data['phone'],pincode=form1.cleaned_data['pincode'],
            patient_status=form1.cleaned_data['patient_status'])
            
            form1.save()
        
           
            s=PatientStatus.objects.create(
                user=request.user,
                center=request.user.center,
                
                patient=form1,
                bed=form2.save()
                
              

                )
            
            s.save()
            return redirect('dashboard')
        else:
            HttpResponse('invalid')
    else:
        form1=NewPatient()
        form2=NewBedcfltc()
    return render(request,'new/cfltcpatient.html',{'form1':form1,'form2':form2,'patients':patients})




def newpatientdom(request):
    # r=Bed.objects.filter(user=request.user,bed_availability=free,ward_no=None,icu_no=None,ventilator_no=None)
    patient_list=[]
    included_patients=Patient.objects.all()
    for i in included_patients:
        patient_list.append(i.patient.id)
    patients=Patient_Register.objects.exclude(id__in=patient_list)

    if request.method=='POST':
        form1=NewPatient(request.POST)
        form2=NewBeddom(request.POST)
        patient=request.POST.get('patient')
        print(patient)
        if form1.is_valid() and form2.is_valid():
            patient_hos_id=request.POST.get('patient_hos_id')
            name=request.POST.get('name')
            adhar=request.POST.get('adhar')
            phone=request.POST.get('phone')
            gender=request.POST.get('gender')

            bed_no=request.POST.get('bed_no')
            ward_no=request.POST.get('ward_no')
            floor_no=request.POST.get('floor_no')
            patient=Patient_Register.objects.get(id=patient)
            print(patient)
            form1=Patient(user=request.user,center=request.user.center,patient=patient,patient_hos_id=form1.cleaned_data['patient_hos_id'],
            name=form1.cleaned_data['name'],adhar=form1.cleaned_data['adhar'],gender=form1.cleaned_data['gender'],phone=form1.cleaned_data['phone'],pincode=form1.cleaned_data['pincode'],
            patient_status=form1.cleaned_data['patient_status'])
            
            form1.save()

            
        
           
            s=PatientStatus.objects.create(
                user=request.user,
                center=request.user.center,
                
                patient=form1,
                bed=form2.save()
                
              

                )
            
            s.save()
            return redirect('dashboard')
        else:
            HttpResponse('invalid')
    else:
        form1=NewPatient()
        form2=NewBeddom()
    return render(request,'new/domipatient.html',{'form1':form1,'form2':form2,'patients':patients})



def newpatienthome(request):
    # r=Bed.objects.filter(user=request.user,bed_availability=free,ward_no=None,icu_no=None,ventilator_no=None)
    patient_list=[]
    included_patients=Patient.objects.all()
    for i in included_patients:
        #print(i.patient.id)
        patient_list.append(i.patient.id)
    patients=Patient_Register.objects.exclude(id__in=patient_list)
    if request.method=='POST':
        form1=NewPatient(request.POST)
        # form2=NewBeddom(request.POST)
        patient=request.POST.get('patient')
        print(patient)
        home=Home.objects.get(user=request.user)
        patient=Patient_Register.objects.get(id=patient)
        print(patient)
        if form1.is_valid():
            frm=Patient(user=request.user,home=home,patient=patient,patient_hos_id=form1.cleaned_data['patient_hos_id'],
            name=form1.cleaned_data['name'],adhar=form1.cleaned_data['adhar'],gender=form1.cleaned_data['gender'],phone=form1.cleaned_data['phone'],pincode=form1.cleaned_data['pincode'],
            patient_status=form1.cleaned_data['patient_status'])

            frm.save()

            # bed_no=request.POST.get('bed_no')
            # ward_no=request.POST.get('ward_no')
            # floor_no=request.POST.get('floor_no')

        
           
            s=PatientStatus.objects.create(
                user=request.user,
                home=request.user.home,
                
                patient_status=frm.patient_status,
                patient=frm,
                # bed=form2.save()
                
              

                )
            
            s.save()
            return redirect('dashboard')
        else:
            HttpResponse('invalid')
    else:
        form1=NewPatient()
        # form2=NewBeddom()
    return render(request,'new/homepatient.html',{'form1':form1,'patients':patients})

def patientshome(request):
    h=PatientStatus.objects.filter(user=request.user)
    return render(request,'home/patients.html',{'list':h})

def centerpatients(request):
    c=PatientStatus.objects.filter(user=request.user)
    
    return render(request,'home/centerpatients.html',{'list':c})


def covid_disese(request,id):
    patient=PatientStatus.objects.get(id=id)
    covi=Disease.objects.filter(patient=patient.patient)
    print(covi)
    return render(request,'home/covid_details.html',{'list':covi})


def patient_diesease(request,id):
    p=PatientStatus.objects.get(id=id)

    if request.method=='POST':
        form=DiseaseForm(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.patient=p.patient
            # p_form.center=request.user.home
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=DiseaseForm()
    return render(request,'hospital/patient_disease.html',{'form':form})


def add_vaccine(request,id):
    p=PatientStatus.objects.get(id=id)

    if request.method=='POST':
        form=VaccineForm(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.patient=p.patient
            # p_form.center=request.user.center
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=VaccineForm()
    return render(request,'vaccine/add_vaccine.html',{'form':form})


def center_vaccine_list(request):
    c_va=Vaccine.objects.filter(user=request.user)
    return render(request,'vaccine/center_vaccine_list.html',{'c_va':c_va})

def all_vaccine(request):
    all_v=Vaccine.objects.all()
    return render(request,'vaccine/all_vaccine.html',{'all_v':all_v})

def update_vaccine(request,id):
    Update = Vaccine.objects.get(id=id)
    print(Update)
    form= VaccineForm(instance=Update)
    if request.method=='POST':
        form= VaccineForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'vaccine/vaccine_update.html',{'form':form})



def view_patients(request):
    all_patients=PatientStatus.objects.filter(patient_status='positive').order_by('-id')
    print(all_patients)
    return render(request,'dmo/view_patients.html',{'all_patients':all_patients})



def view_hospital_doctors(request):
    doctors=Doctor.objects.filter(center=request.user.center)
    print(doctors)
    return render(request,'hospital/view_doctors.html',{'doctors':doctors})