from django.shortcuts import render,redirect
from patient.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
import random
import string
from django.core.mail import send_mail
from doctor.models import *
from home.models import *

# Create your views here.


def view_patients(request):
    patients=Patient.objects.filter(user=request.user)
    print(patients)
    return render(request,'home/view_patients.html',{'patients':patients})
