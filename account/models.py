from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
# from lab.models import *


hospital='Hospital'
cfltc='CFLTC'
csltc='CSLTC'
domicile='Domicile'


ceter_types=[(hospital,'Hospital'),(cfltc,'CFLTC'),(csltc,'CSLTC'),(domicile,'Domicle')]

#authority
private='Private'
govermnet='Government'
authority_types=[(private,'Private'),(govermnet,'Government')]

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

category_a='category a'
category_b='category_b'
category_c='category_c'
category=[(category_a,'category_a'),(category_b,'category_b'),(category_c,'category_c')]

avilable='available'
not_available='not_available'

available=[(avilable,'avilable'),(not_available,'not_available')]


Male = 'Male'
Female = 'Female'
Other='Oother'
GENDER_CHOICES = [
        (Male,'Male'),
        (Female,'Female'),
        (Other,'Other')
]

muncipality = 'Muncipality'
corparation = 'Corparation'
panchayath='Panchayath'
authority_types = [
        (muncipality,'Muncipality'),
        (corparation,'Corparation'),
        (panchayath,'panachayath')
]

anigen='antigen'
rtpcr='RTPCR'

test_names=[(anigen,'antigen'),(rtpcr,'rtpcr')]


avilable='available'
not_available='not_available'

available=[(avilable,'avilable'),(not_available,'not_available')]

negative='Negative'
positive='Postitive'

results=[(negative,'Negative'),(positive,'Postitive'),]

nasopharyngeal_swab='Nasopharyngeal_Swab'
oropharyngeal_swab='Oropharyngeal_Swab'
specimens=[(nasopharyngeal_swab,'Nasopharyngeal_Swab'),(oropharyngeal_swab,'Oropharyngeal_Swab')]

first_dose='first_dose'
second_dose='second_dose'
dose_nos=[(first_dose,'first_dose'),(second_dose,'second_dose')]


yes='yes'
no='no'
add=[(yes,'yes'),(no,'no'),]

hospital='hospital'
private='private'

lab_type=[(hospital,'hospital'),(private,'private')]


Thiruvananthapuram = 'Thiruvananthapuram'
Kollam = 'Kollam'
Alappuzha= 'Alappuzha'
Pathanamthitta = 'Pathanamthitta'
Kottayam = 'Kottayam'
Idukki = 'Idukki'
Ernakulam = ' Ernakulam'
Thrissur= 'Thrissur'
Palakkad = 'Palakkad'
Malappuram = 'Malappuram'
Kozhikode = ' Kozhikode'
Wayanadu= 'Wayanadu'
Kannur = 'Kannur'
Kasaragod = 'Kasaragod'

District_name =(
    (Thiruvananthapuram , 'Thiruvananthapuram'),
    (Kollam , 'Kollam'),
    (Alappuzha , 'Alappuzha'),
    (Pathanamthitta , 'Pathanamthitta'),
    (Kottayam , 'Kottayam'),
    (Idukki , 'Idukki'),
    ( Ernakulam , ' Ernakulam'),
    (Thrissur, 'Thrissur'),
    (Palakkad , 'Palakkad'),
    (Malappuram , 'Malappuram'),
    (Kozhikode, ' Kozhikode'),
    (Wayanadu, 'Wayanadu'),
    (Kannur , 'Kannur'),
    (Kasaragod , 'Kasaragod')
)

# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self):
        return str(self.name)
    


class Center(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    center_name=models.CharField(max_length=50)
    authority_type=models.CharField(max_length=50,choices=authority_types,default=govermnet)
    center_pincode=models.PositiveIntegerField()
    center_place=models.CharField(max_length=60)
    center_type=models.CharField(max_length=50,choices=ceter_types,)
    center_ideantification_proof=models.FileField(upload_to='center_proof')
    center_phone=PhoneNumberField()
    center_photo=models.ImageField(upload_to='center_photo')
    status_appruval=models.BooleanField(default=False)

    def __str__(self):
        return str(self.center_name)

class Patient_Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    phonenumber=PhoneNumberField()
    adhar=models.PositiveIntegerField(unique=True)
    pincode=models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    doctor_photo=models.ImageField(upload_to='doctor_iamge')
    phonenumber=PhoneNumberField()
    doctor_certificate=models.FileField(upload_to='doctor_certificate')
    qualification=models.CharField(max_length=60)
    address=models.TextField()
    doctor_avilability=models.CharField(max_length=50,blank=True,null=True,choices=available)
    online_avilable=models.BooleanField(default=False)
    status_appruval=models.BooleanField(default=False)


    def __str__(self):
        return str(self.name)





class Home(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    authority_type=models.CharField(max_length=30,choices=authority_types,)
    authority_name=models.CharField(max_length=50)
    ward_no=models.PositiveIntegerField()
    village=models.CharField(max_length=50)
    pincode=models.PositiveIntegerField()
    phonenumber=PhoneNumberField()
    status_appruval=models.BooleanField(default=False)

    def __str__(self):
        return str(self.authority_type)

class UserRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    phonenumber=PhoneNumberField()
    adhar=models.PositiveIntegerField(unique=True)
    pincode=models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)

class Lab(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    lab_name=models.CharField(max_length=50)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    loaction=models.CharField(max_length=100,blank=True,null=True)
    lab_district=models.CharField(max_length=40,blank=True,null=True,choices=District_name,default=Thrissur)
    lab_pincode=models.IntegerField()
    lab_type=models.CharField(max_length=30,blank=True,null=True,choices=lab_type)
    lab_certificate=models.FileField(upload_to='lab_certificate')
    lab_avilability=models.CharField(max_length=30,choices=available,default=available)
    phonenumber=PhoneNumberField(blank=True,null=True)
    photo_of_lab=models.ImageField(upload_to='lab_image',default="lab.jpg")
    status_appruval=models.BooleanField(default=False)

    def __str__(self):
        return str(self.center)


class DMO(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    phonenumber=PhoneNumberField()
    adhar=models.PositiveIntegerField(unique=True)
    pincode=models.PositiveIntegerField()
    status_appruval=models.BooleanField(default=False)


    def __str__(self):
        return str(self.adhar)