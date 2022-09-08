from django.contrib import admin
from .models import users,posts
# Register your models here.
@admin.register(users)
class usersADMIN(admin.ModelAdmin):
    list_display = ['id','name','email','password','address','account','userimg','gender']



@admin.register(posts)
class usersADMIN(admin.ModelAdmin):
    list_display = ['id','user','postdata','postimg','dateofpost']