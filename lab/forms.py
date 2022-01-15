from django import forms
from django.db.models import fields
from django.db.models.fields import files
from django.forms.widgets import EmailInput, PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import *

class LabstatusForm(forms.ModelForm):
    class Meta:
        model=Lab
        fields=('lab_avilability',)

class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields=('test_id','test_name','test_cost','test_avilability')




