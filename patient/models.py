from django.db import models
from account.models import *
from django.utils import timezone
from datetime import datetime, timedelta
from lab.models import *
from center.models import *
# Create your models here.
def utc_tomorrow():
    return datetime.utcnow() + timedelta(days=1)

class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    home=models.ForeignKey(Home,on_delete=models.CASCADE,blank=True,null=True)
    complaint=models.TextField()
    replay=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(default=datetime.utcnow,blank=True,null=True)
    # replay_date=models.DateTimeField(default=timezone.now)    
    replay_date=models.DateTimeField(default=utc_tomorrow,blank=True,null=True)
    solved='solved'
    un_solved='un_solved'
    solve_statuses=[
        ('solved',solved),
        ('un_solved',un_solved)
    ]
    solve_status=models.CharField(max_length=20,choices=solve_statuses,default=un_solved)
    replay_status=models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

class Chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
    doubts=models.TextField()
    patient=models.ForeignKey(PatientStatus,on_delete=models.CASCADE,blank=True,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    replay=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)
    replay_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user)
