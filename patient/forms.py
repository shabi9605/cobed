from django import forms
from lab.forms import *

from .models import *
from django.contrib.auth.models import User

class ComplaintForm(forms.ModelForm):
    
    class Meta:
        model=Complaint
        fields=('center','home','complaint',)

class UpdateComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('solve_status','complaint','created_date')


class ComplaintPassDmo(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('replay_status',)

class ChatForm(forms.ModelForm):
    class Meta:
        model=Chat
        fields=('doubts',)

class UpdateChatForm(forms.ModelForm):
    class Meta:
        model=Chat
        fields=('doubts','replay','created_date')


