from django import forms
from django.db.models import fields
from django.db.models.enums import Choices
from django.forms.widgets import EmailInput, PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('patient','name','email','age','adhar','phone','gender','phone','house_name',
    'place','authority_type','authority_name','ward_no','village','district','pincode')

    def clean(self):
      super(PatientForm, self).clean()

      # getting username and password from cleaned_data
      adhar = self.cleaned_data.get('adhar')
      
      # validating the username and password
      if adhar == 12:
         self._errors['adhar'] = self.error_class(['Invlaid adhar number'])

      

      return self.cleaned_data




class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('name','email','age','adhar','phone','gender','phone','house_name',
    'place','authority_type','authority_name','ward_no','village','district','pincode',)


class StatusFormLab(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('test_id','test_name','patient_status')
negative='negative'
positive='positive'
death='death'
death_with_in_onemonth='death with in one month'
discharged='discharged'
shifted_to_CFLTC='shifted to CFLTC'
shifted_to_CSLTC='shifted to CSLTC'
shifted_to_domociline='shifted_to_domociline'
shifted_to_home='shifted_to_home'
patient_present_status=[(death_with_in_onemonth,'death_with_in_onemonth'),(discharged,'discharged'),(shifted_to_CFLTC,'shifted_to_CFLTC'),
(shifted_to_CSLTC,'shifted_to_CSLTC'),(shifted_to_domociline,'shifted_to_domociline'),
(shifted_to_home,'shifted_to_home'),(death,'death'),(positive,'positive'),(negative,'negative')]


class UpdateStatusFormLab(forms.ModelForm):
    positive='positive'
    death='death'
    patient_present_status=[(positive,'positive'),(negative,'negative')]
    patient_status=forms.ChoiceField(choices=patient_present_status,required=True)
    class Meta:
        model=Patient
        fields=('test_id','test_name','patient_status')

class PatientFormHospital(forms.ModelForm):
    class Meta:
        model=PatientStatus
        fields=('patient_status','category',)



class BedForm(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','room_no','floor_no',
        'bed_with_oxygen','bed_gender')

class BedForm1(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','floor_no','ward_no',
       'bed_with_oxygen','bed_gender')

class BedForm2(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','floor_no',
       'icu_no','bed_with_oxygen','bed_gender')

class BedForm3(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','floor_no',
       'ventilator_no','bed_with_oxygen','bed_gender')


# class PatientBedForm(forms.ModelForm):
#     class Meta:
#         model=Bed
#         fields=('bed_no','room_no','floor_no','ward_no',
#         'icu_no','ventilator_no','bed_with_oxygen','bed_gender')


class UpdateBedForm1(forms.ModelForm):
    class Meta:
        model=PatientStatus
        fields=('bed','patient_status','category')


class UpdateBedForm2(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','ward_no','bed_gender',)

class UpdateBedForm3(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','icu_no','bed_gender',)

class UpdateBedForm4(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','ventilator_no','bed_gender',)



class NewPatient(forms.ModelForm):
    patient_hos_id=forms.CharField(label='Patient Hospital ID')
    class Meta:
        model=Patient
        fields=('patient_hos_id','name','adhar','gender','phone','pincode','patient_status',)

class NewBed(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','room_no','floor_no','bed_availability','ward_no','icu_no','ventilator_no')

class NewBedcfltc(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','room_no','floor_no','bed_availability','ward_no',)

class NewBeddom(forms.ModelForm):
    class Meta:
        model=Bed
        fields=('bed_no','room_no','floor_no','bed_availability','bed_gender',)



class homepatient(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('name','adhar','gender','phone','pincode','house_name',)

class DiseaseForm(forms.ModelForm):
    class Meta:
        model=Disease
        fields=('pre_covid_dis','post_covid_dis')

class VaccineForm(forms.ModelForm):
    # first_dose_date=forms.DateField(label='Fisrt Dose Date',widget=NumberInput(attrs={'type':'date'}))
    # second_dose_date=forms.DateTimeField(label='Second Dose Date',widget=NumberInput(attrs={'type':'date'}),required=False)

    class Meta:
        model=Vaccine
        fields=('adhar','vaccine_name','dose_no','fisrst_dose_date','second_dose_date')

class UpdateVaccineForm(forms.ModelForm):
    first_dose_date=forms.DateField(label='Fisrt Dose Date',widget=NumberInput(attrs={'type':'date'}))
    second_dose_date=forms.DateField(label='Second Dose Date',widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model=Vaccine
        fields=('patient','adhar','vaccine_name','dose_no',
        'fisrst_dose_date','second_dose_date',)

