from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Center
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.utils import timezone
from lab.models import *
from center.models import *

# Create your models here.

class Death(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    death_date=models.DateTimeField(default=timezone.now)
    reason=models.TextField(default='covid-19')
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    appruval=models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient)