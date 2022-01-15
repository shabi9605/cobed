from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from account.models import *
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.
free='free'
occupied='occupied'
bed_av=[(free,'free'),(occupied,'occupied')]

class Patient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    lab=models.ForeignKey(Lab,on_delete=models.CASCADE,blank=True,null=True)
    home=models.ForeignKey(Home,on_delete=models.CASCADE,blank=True,null=True)
    patient=models.ForeignKey(Patient_Register,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    adhar=models.PositiveIntegerField(unique=True,blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,blank=True,null=True)
    phone=PhoneNumberField(blank=True,null=True)
    house_name=models.CharField(max_length=40,blank=True,null=True)
    place=models.CharField(max_length=70,blank=True,null=True)
    authority_type=models.CharField(max_length=30,choices=authority_types,blank=True,null=True)
    authority_name=models.CharField(max_length=100,blank=True,null=True)
    ward_no=models.PositiveIntegerField(blank=True,null=True)
    village=models.CharField(max_length=50,blank=True,null=True)
    district=models.CharField(max_length=50,default=Thrissur)
    pincode=models.PositiveIntegerField(blank=True,null=True)
    patient_hos_id=models.PositiveIntegerField(blank=True,null=True)
    test_id=models.PositiveIntegerField(blank=True,null=True)
    test_date=models.DateField(auto_now_add=True,blank=True,null=True)
    test_name=models.CharField(max_length=50,choices=test_names,default=rtpcr)
    patient_status=models.CharField(max_length=30,choices=patient_present_status,blank=True,null=True)

    created_date=models.DateField(auto_now_add=True)

    
    def __str__(self):
        return str(self.name)





class Bed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    # patient_status=models.ForeignKey(PatientStatus,on_delete=models.CASCADE,blank=True,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,blank=True,null=True)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    bed_no=models.PositiveIntegerField(blank=True,null=True)
    ward_no=models.PositiveIntegerField(blank=True,null=True)
    floor_no=models.PositiveIntegerField(blank=True,null=True)
    room_no=models.PositiveIntegerField(blank=True,null=True)
    icu_no=models.PositiveIntegerField(blank=True,null=True)
    ventilator_no=models.PositiveIntegerField(blank=True,null=True)
    bed_availability=models.CharField(max_length=30,choices=bed_av,default=free)
    bed_with_oxygen=models.CharField(max_length=30,choices=add,default=no)
    bed_gender=models.CharField(max_length=30,choices=GENDER_CHOICES,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.bed_no)

class PatientStatus(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,blank=True,null=True)
    bed=models.ForeignKey(Bed,on_delete=models.CASCADE,blank=True,null=True)
    home=models.ForeignKey(Home,on_delete=models.CASCADE,blank=True,null=True)
    patient_status=models.CharField(max_length=30,choices=patient_present_status,default=positive,blank=True,null=True)
    category=models.CharField(max_length=40,choices=category,blank=True,null=True)
   
    created_date=models.DateField(auto_now_add=True)
    # date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.patient)




covishiled='covisheild'
covaxine='covaxine'
sputinic='sputinic'
vacine_types=[(covishiled,'covisheild'),
        (covaxine,'covaxine'),
        (sputinic,'sputinic')]

first_dose='first_dose'
second_dose='second_dose'
dose_nos=[(first_dose,'first_dose'),(second_dose,'second_dose')]

# home_quratine='home_quratine'
# hospital_quratine='hospital_quratine'
# centers_quratine='centers_quratine'
# quratine_details=[(home_quratine,'home_quratine'),(hospital_quratine,'hospital_quratine'),
# (centers_quratine,'centers_quratine')]

class Disease(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,blank=True,null=True)
    pre_covid_dis=models.CharField(max_length=200)
    post_covid_dis=models.CharField(max_length=200)
    created_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user)


class Vaccine(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,blank=True,null=True)
    adhar=models.PositiveIntegerField()
    vaccine_name=models.CharField(max_length=50,choices=vacine_types,default=covaxine)
    dose_no=models.CharField(max_length=40,choices=dose_nos,default=first_dose)
    fisrst_dose_date=models.DateTimeField(default=timezone.now)
    second_dose_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return str(self.patient)