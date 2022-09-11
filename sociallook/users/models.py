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
    



class posts(models.Model):
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    postdata = models.TextField(blank=True)
    postimg = models.ImageField(upload_to='postimg/',null=True)
    dateofpost = models.DateTimeField(auto_now_add=True,blank=True)



class activity(models.Model):
    whofollow = models.ForeignKey(users,on_delete=models.CASCADE,related_name='follow')
    whomtofollow = models.ForeignKey(users,on_delete=models.CASCADE,related_name='follower')
    dateoffollow = models.DateTimeField(auto_now_add=True,blank=True)



class post_activities(models.Model):
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    post = models.ForeignKey(posts,on_delete=models.CASCADE)
   
    comments = models.TextField()
    dateofpostactivity = models.DateTimeField(auto_now_add=True,blank=True)