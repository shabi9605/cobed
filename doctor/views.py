from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from patient.models import *
# Create your views here.


def death_home(requet):
    d=Death.objects.filter(user=requet.user)
    return render(requet,'doctor/home_death.html',{'d':d})

def patient_death(request):
    if request.method=='POST':
        form=DeathForm(request.POST)
        if form.is_valid():
            user=request.user
            user.save()
            p_form=form.save()
            p_form.user=user
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=DeathForm()
    return render(request,'doctor/patient_death.html',{'form':form})


def update_death(request,id):
    Update = Death.objects.get(id=id)
    print(Update)
    form= DeathFormVerify(instance=Update)
    if request.method=='POST':
        form= DeathFormVerify(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('dashboard')
    return render(request,'doctor/verify.html',{'form':form})


def death_details(request):
    d=Death.objects.filter(center=request.user.doctor.center)
    return render(request,'doctor/death_details.html',{'d':d})



def view_deaths(request):
    deaths=Death.objects.filter(appruval=False)
    return render(request,'doctor/view_death.html',{'deaths':deaths})


def approved_deaths(request):
    deaths=Death.objects.filter(appruval=True)
    return render(request,'doctor/view_death.html',{'deaths':deaths})



def chat(request):
    print(request.user.doctor.center)
    patients=PatientStatus.objects.filter(center=request.user.doctor.center)
    print(patients)
    if request.method=="POST":
        patient=request.POST.get('patient')
        chat=request.POST.get('chat')
        patient=PatientStatus.objects.get(patient=patient)
        chat=Chat.objects.create(
            patient=patient,
            doubts=chat,
            user=request.user

        )
        chat.save
        return redirect('view_my_chat')
    return render(request,'doctor/chat.html',{'patients':patients})


def view_my_chat(request):
    my_chat=Chat.objects.filter(user=request.user)
    received_chat=Chat.objects.filter(doctor=request.user.doctor)
    print(my_chat)
    return render(request,'doctor/my_chats.html',{'my_chat':my_chat,'received_chat':received_chat})



def patient_chat(request):
    print(request.user.patient_register)
    patient=request.user.patient_register
    patient=Patient.objects.get(patient=patient)
    print(patient.center)
    patients=Doctor.objects.filter(center=patient.center)
    print(patients)
    if request.method=="POST":
        doctor=request.POST.get('doctor')
        chat=request.POST.get('chat')
        doctor=Doctor.objects.get(id=doctor)
        chat=Chat.objects.create(
            doctor=doctor,
            doubts=chat,
            user=request.user

        )
        chat.save
        return redirect('view_patient_chat')
    return render(request,'doctor/patient_chat.html',{'patients':patients})



def view_patient_chat(request):
    my_chat=Chat.objects.filter(user=request.user)
    patient=request.user.patient_register
    patient=Patient.objects.get(patient=patient)
    received_chat=Chat.objects.filter(patient__patient=patient)
    print(my_chat)
    return render(request,'doctor/my_chats.html',{'my_chat':my_chat,'received_chat':received_chat})
