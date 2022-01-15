from django.shortcuts import render,redirect
from patient.models import *
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.db.models import Q
import random
import string
from django.core.mail import send_mail
from doctor.models import *
from home.models import *
from account.models import *
from center.models import *
from center.forms import *
# Create your views here.


def add_test(request):
    if request.method=='POST':
        form=TestForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            lab=request.user.lab
            f=form.save()
            f.user=user
            f.lab=lab
            f.save()
            messages.success(request,'sucesfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=TestForm()
    return render(request,'test/add_test.html',{'form':form})


def test_list(request):
    t=Test.objects.filter(user=request.user)
    return render(request,'test/test_list.html',{'t':t})

def test_update(request,id):
    Update = Test.objects.get(id=id)
    print(Update)
    form= TestForm(instance=Update)
    if request.method=='POST':
        form= TestForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'test/update_test.html',{'form':form})

def test_delete(request,id):
    u=Test.objects.get(id=id)
    u.delete()
    return redirect('test_list')

def lab_data(request):
    l=Lab.objects.filter(user=request.user)
    return render(request,'lab/lab_data.html',{'list':l})

def update_availbility(request,id):
    Update = Lab.objects.get(id=id)
    print(Update)
    form= LabstatusForm(instance=Update)
    if request.method=='POST':
        form= LabstatusForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'lab/lab_status_update.html',{'form':form,})


def add_patient_lab(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        
        if form.is_valid():
            user=request.user

            user.save()
            lab=request.user.lab
            lab=lab
            p_form=form.save()
            p_form.user=user
            # p_form.center=request.user.center
            p_form.save()
            # s=Patient.objects.create(
            #     patient=p_form
            # )
            # s.save()

            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=PatientForm()
    return render(request,'lab/patient_register.html',{'form':form})

def lab_patient_view(request):
    lab_p=Patient.objects.filter(user=request.user)
    return render(request,'lab/lab_patient_list.html',{'list':lab_p})


def update_patient_lab(request,id):
    Update = Patient.objects.get(id=id)
    print(Update)
    form= UpdatePatientForm(instance=Update)
    if request.method=='POST':
        form= UpdatePatientForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'lab/lab_patient_update.html',{'form':form,'patient':Update})

def delete_patient_lab(request,id):
    deletep = Patient.objects.get(id=id)
    deletep.delete()
    messages.success(request,'Record deleted succefully')
    return redirect('dashboard')

def patient_status_list(request):
    s=Patient.objects.filter(user=request.user)
    return render(request,'lab/status_list.html',{'list':s})

def update_patientstatus_lab(request,id):
    Update = Patient.objects.get(id=id)
    print(Update)
    form= UpdateStatusFormLab(instance=Update)
    if request.method=='POST':
        form= UpdateStatusFormLab(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'lab/patient_status_update.html',{'form':form,'patient':Update})

# def all_patients(request):
#     all=Patient.objects.all()
#     return render(request,'all_patient.html',{'all':all})

# def doctor_patient(request):
#     all=Patient.objects.filter(quratine_detail=request.user.doctor.center)
#     return render(request,'doctor/all_patient.html',{'all':all})

# def search_patients(request):
#     try:
#         if request.method=='GET':
#             q=request.GET.get('query')
#             lab_p=Patient.objects.filter(name__icontains=q,user=request.user)|Patient.objects.filter(adhar__icontains=q,user=request.user)
#             return render(request,'lab/lab_patient_list.html',{'lab_p':lab_p})
#         return render(request,'lab/lab_patient_list.html',)
#     except:
#         pass

