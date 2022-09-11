from django.contrib import admin
from .models import users,posts,activity,post_activities
# Register your models here.
@admin.register(users)
class usersADMIN(admin.ModelAdmin):
    list_display = ['id','name','email','password','address','account','userimg','gender']



@admin.register(posts)
class postsADMIN(admin.ModelAdmin):
    list_display = ['id','user','postdata','postimg','dateofpost']


@admin.register(activity)
class activityADMIN(admin.ModelAdmin):
    list_display = ['id','whofollow','whomtofollow','dateoffollow']

@admin.register(post_activities)
class post_activityADMIN(admin.ModelAdmin):
    list_display = ['id','comments','post','user']


