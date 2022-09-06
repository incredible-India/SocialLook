from django.db import models
import datetime 
# Create your models here.

class users(models.Model):
    GENDER_CHOICES	=	(('male',	'Male'),('female',	'Female'),('transgender',	'Transgender'),)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=250)
    address = models.TextField()
    account = models.DateTimeField(default=datetime.datetime.now(), blank=True,null=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='male')
    userimg = models.ImageField(upload_to='userimg/' ,null=True)
    