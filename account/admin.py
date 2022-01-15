from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header='Cobed Administration'

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message']
admin.site.register(Contacts,ContactAdmin)

class CenterAdmin(admin.ModelAdmin):
    list_display=['center_name','center_type','authority_type','center_phone',
    'center_ideantification_proof','status_appruval']

admin.site.register(Center,CenterAdmin)


class PatientRegisterAdmin(admin.ModelAdmin):
    list_display=['user','phonenumber','adhar','pincode']
admin.site.register(Patient_Register,PatientRegisterAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display=['user','center','phonenumber','doctor_certificate','qualification','doctor_avilability']
admin.site.register(Doctor,DoctorAdmin)


class DMOAdmin(admin.ModelAdmin):
    list_display=['user','phonenumber','adhar','pincode']
admin.site.register(DMO,DMOAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display=['user','phonenumber','adhar','pincode']
admin.site.register(UserRegister,UserAdmin)


class LabAdmin(admin.ModelAdmin):
    list_display=['user','lab_name','center','lab_pincode','phonenumber','status_appruval']
admin.site.register(Lab,LabAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display=['user','name','authority_type','authority_name','ward_no','status_appruval']
admin.site.register(Home,HomeAdmin)

