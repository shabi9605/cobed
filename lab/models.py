from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from account.models import *
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
# Create your models here.

class Test(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    lab=models.ForeignKey(Lab,on_delete=models.CASCADE,blank=True,null=True)
    test_id=models.PositiveIntegerField()
    test_name=models.CharField(max_length=50,choices=test_names,default=anigen)
    test_cost=models.PositiveIntegerField()
    test_avilability=models.CharField(max_length=50,choices=available,blank=True,null=True)
    created_date=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return str(self.test_name)

