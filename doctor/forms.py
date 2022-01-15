from functools import cmp_to_key
from django import forms
from django.forms import fields
from django.forms.widgets import SelectDateWidget
from .models import *
from django.contrib.auth.models import User

class DeathForm(forms.ModelForm):
    death_date=forms.DateTimeField(label='Death Date',widget=SelectDateWidget)
    class Meta:
        model=Death
        fields=('patient','death_date','reason','center',)

class DeathFormVerify(forms.ModelForm):
    death_date=forms.DateTimeField(label='Death Date',widget=SelectDateWidget)
    class Meta:
        model=Death
        fields=('patient','death_date','reason','center','appruval')
