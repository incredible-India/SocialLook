from django.shortcuts import render
from users.middleware import checkingUserAuthentication
from django.utils.decorators import method_decorator
from django.db.models import Q
from users.models import users,posts,post_activities,activity
# Create your views here.

@(checkingUserAuthentication)
def index(request):
    if(request.isauth):

        user = users.objects.all()

        currentuser = users.objects.get(email=request.session['email'])

       
        #if this post does not belong to user then check user follow that person or not  
        #cheking the user post only so that he can his post
        upost = posts.objects.filter(user=currentuser)

        followusers = activity.objects.filter(whofollow=currentuser)
        
        tempuserid=[]

        userspost = []

        for i in followusers:
            tempuserid.append(i.whomtofollow.id)
        

        if len(tempuserid)==0:
            total=False
        else:
            for j in tempuserid:
                userspost.append(posts.objects.filter(user=users.objects.get(id=j)))
            
        
        if len(userspost) == 0:
            total=False
        else:
            total=userspost
        


        return render(request,'home/welcome.html',{'username':
        request.name,'user':user
        ,'id':currentuser.id,
        'upost':upost,
        'total' : total})
    else:
        return render(request,'home/home.html')




