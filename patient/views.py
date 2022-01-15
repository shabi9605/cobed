from django.shortcuts import render,redirect
from doctor.models import Death
from lab.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404, request
from django.urls import reverse
from django.contrib import messages
from .forms import *
import datetime
from datetime import datetime, timedelta

from datetime import date
from center.models import *

def view_patient(request):
    c=PatientStatus.objects.filter(patient__adhar=request.user.patient_register.adhar)
    return render(request,'patient/patient.html',{'c':c})

def complaint(request):
    patient=request.user.patient_register
    # p=Patient.objects.get(patient=patient)
    #p=PatientStatus.objects.get(patient=request.user.patient_register)
    # print(p.center)

    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            # p_form.center=p.center
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=ComplaintForm()
    return render(request,'patient/complaint.html',{'form':form})

def complaint_view(request):
    com=Complaint.objects.all().filter(center=request.user.center)
    return render(request,'patient/complaint_list.html',{'com':com})

def complaint_replay_view(request):
    com=Complaint.objects.filter(user=request.user)
    return render(request,'patient/com_replay_view.html',{'com':com})

def dmo_complaint(request):
    c=Complaint()
    futuredate = datetime.now() + timedelta(days=1)
    print(futuredate)
    now = datetime.now()
    print(now)
    print(c.replay_date)
    if Complaint.objects.filter(replay_status=False) or Complaint.objects.filter(replay_date=now):
        com=Complaint.objects.all()
        return render(request,'dmo/dmo_complaint_view.html',{'com':com})
    return render(request,'dmo/dmo_complaint_view.html')
 

def complaint_replay(request,id):
    Update = Complaint.objects.get(id=id)
    print(Update)
    form= UpdateComplaintForm(instance=Update)
    if request.method=='POST':
        form= UpdateComplaintForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'complaint/complaint_replay.html',{'form':form,})


def complaint_pass_dmo(request,id):
    Update = Complaint.objects.get(id=id)
    print(Update)
    form= ComplaintPassDmo(instance=Update)
    if request.method=='POST':
        form= ComplaintPassDmo(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'complaint/complaint_replay.html',{'form':form,})


def chat(request):
    p=PatientStatus.objects.get(patient__adhar=request.user.patient_register.adhar)
    if request.method=='POST':
        form=ChatForm(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.center=p.center
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=ChatForm()
    return render(request,'patient/chat.html',{'form':form})

def chat_view(request):
    c=Chat.objects.filter(center=request.user.doctor.center)
    return render(request,'doctor/chat_list.html',{'c':c})

def chat_replay_view(request):
    c=Chat.objects.filter(user=request.user)
    return render(request,'patient/chat_replay_view.html',{'c':c})

def inproperdeath(request):
    d=Death.objects.filter(appruval=False).count()
    return render(request,'dmo/inproper.html',{'d':d})



def chat_replay(request,id):
    Update = Chat.objects.get(id=id)
    print(Update)
    form= UpdateChatForm(instance=Update)
    if request.method=='POST':
        form= UpdateChatForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'doctor/chat_replay.html',{'form':form,})



def dmo_view_complaint(request):
    complaints=Complaint.objects.filter(replay_status=True)
    return render(request,'patient/complaint_list.html',{'com':complaints})




def home_view_complaint(request):
    complaints=Complaint.objects.filter(home=request.user.home)
    return render(request,'patient/home_view_complaint.html',{'com':complaints})




def view_details(request):
    details=Patient_Register.objects.get(user=request.user)
    return render(request,'patient/view_profile.html',{'details':details})


def view_all_patients(request):
    patients=Patient.objects.all()
    return render(request,'doctor/view_all_patients.html',{'patients':patients})