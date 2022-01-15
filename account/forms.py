
from django import forms
from django.forms.widgets import EmailInput, PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
   
    username=forms.EmailField(label='Emailid',required=True,widget=forms.EmailInput)
    password1=forms.CharField(help_text=None,widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Center
        fields=('center_name','authority_type','center_pincode','center_place','center_type','center_phone',
    'center_ideantification_proof','center_photo')

    
    def clean(self):
        super(ProfileForm, self).clean()

      # getting username and password from cleaned_data
        center_pincode = self.cleaned_data.get('center_pincode')
      
      # validating the username and password
        if center_pincode == 6:
            self._errors['center_pincode'] = self.error_class(['Invlaid Pincode'])

        return self.cleaned_data


class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    class Meta:
        model=User
        fields=('username',)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Center
        fields=('center_name','authority_type','center_pincode','center_place','center_type','center_phone',
    'center_ideantification_proof','center_photo')



class Patient_RegisterForm(forms.ModelForm):
    class Meta:
        model=Patient_Register
        fields=('name','phonenumber','adhar','pincode')
        

class UpdatePatientRegisterForm(forms.ModelForm):
    class Meta:
        model=Patient_Register
        fields=('name','phonenumber',)

class Doctor_RegisterForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=('name','phonenumber','doctor_certificate','qualification',
        'address','doctor_photo','doctor_avilability')

class UpdateDoctorRegisterForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=('name','phonenumber','doctor_photo','address','online_avilable')


class DmoForm(forms.ModelForm):
    class Meta:
        model=DMO
        fields=('name','phonenumber','adhar','pincode')
        

class UpdateDmoForm(forms.ModelForm):
    class Meta:
        model=DMO
        fields=('name','phonenumber','pincode')



class UserFormLab(forms.ModelForm):
   
    username=forms.EmailField(label='Email Id',required=True,widget=forms.EmailInput)
    password1=forms.CharField(help_text=None,widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2')
        
class ProfileFormLab(forms.ModelForm):
    private='private'

    lab_type=[(private,'private')]
    lab_type=forms.ChoiceField(choices=lab_type)
    class Meta:
        model=Lab
        fields=('lab_name','loaction','lab_type','lab_pincode','lab_certificate','photo_of_lab','phonenumber',)

    
    def clean(self):
        super(ProfileFormLab, self).clean()

      # getting username and password from cleaned_data
        lab_pincode = self.cleaned_data.get('lab_pincode')
      
      # validating the username and password
        if lab_pincode == 6:
            self._errors['lab_pincode'] = self.error_class(['Invlaid Pincode'])

        return self.cleaned_data

class UpdateFormLab(forms.ModelForm):
    username=forms.EmailField(help_text=None,label='Username',widget=forms.EmailInput)
    class Meta:
        model=User
        fields=('username',)

class LabForm(forms.ModelForm):
    private='private'

    lab_type=[(private,'private')]
    lab_type=forms.ChoiceField(choices=lab_type)
    class Meta:
        model=Lab
        fields=('lab_name','loaction','lab_type','lab_pincode','lab_certificate','lab_avilability','phonenumber',)

class LabUpdateForm(forms.ModelForm):
    class Meta:
        model=Lab
        fields=('lab_name','loaction','lab_type','lab_certificate','lab_avilability','phonenumber','photo_of_lab')

class HomeForm(forms.ModelForm):
    class Meta:
        model=Home
        fields=('name','authority_type','authority_name','ward_no','village','pincode','phonenumber',)

class HomeProfileForm(forms.ModelForm):
    class Meta:
        model=Home
        fields=('name','authority_type','authority_name','village','pincode','phonenumber',)

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=('name','phonenumber','pincode','adhar')

class UpdateUserRegister(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=('name','phonenumber','pincode')



class LabFormHospital(forms.ModelForm):
    hospital='hospital'
    lab_type=[(hospital,'hospital')]
    lab_type=forms.ChoiceField(choices=lab_type)
    class Meta:
        model=Lab
        fields=('lab_type','center','lab_certificate','lab_avilability','phonenumber','lab_pincode')


class AdminCenterProfileForm(forms.ModelForm):
    class Meta:
        model=Center
        fields=('center_name','status_appruval')

class AdminLabProfileForm(forms.ModelForm):
    class Meta:
        model=Lab
        fields=('lab_name','status_appruval')

class AdminHomeProfileForm(forms.ModelForm):
    class Meta:
        model=Home
        fields=('name','status_appruval')

class AdminDMOProfileForm(forms.ModelForm):
    class Meta:
        model=Home
        fields=('name','status_appruval')

class AdminDoctorProfileForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=('name','status_appruval')