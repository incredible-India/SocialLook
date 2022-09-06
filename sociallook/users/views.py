from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import users
from django.utils.decorators import method_decorator
from .middleware  import checkingUserAuthentication
# Create your views here.



class newuser(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            return HttpResponseRedirect('/')
        else:
            return render(request,'users/create.html')
    
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        if 'is_private' in request.POST:
            userimg = request.FILES['img']
        else:
            userimg = False
        
   

    
        isExistEmail = users.objects.filter(email=email)

        if(len(isExistEmail)>0):
            messages.info(request,'Email already exists you should try to login or use another email')
            return HttpResponseRedirect('/user/newuser/registeration')
        elif(len(name) < 2 or name==''):
            messages.info(request,'Name is too short it should be greater than 2 charters and less than 200 charters')
            return HttpResponseRedirect('/user/newuser/registeration')
        elif(len(password) < 3):
            messages.info(request,'Password is too short..')
            return HttpResponseRedirect('/user/newuser/registeration')
        
        else :
            users.objects.create(name=name, email=email, password=password,address=address,userimg=userimg,gender=gender)

            request.session['email'] = email 
            request.session['name'] = name

            return HttpResponseRedirect('/')

    

        
            



#for the logout function 

class logout(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            del request.session['name']
            del request.session['email']
   
        
        return HttpResponseRedirect('/')


#for the login functions 

class login(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'users/login.html')

    @method_decorator(checkingUserAuthentication)
    def post(self,request):
        if request.isauth:
            return HttpResponse('Invalid Request..')
        
        email = request.POST.get('email')
        password = request.POST.get('password')


        isMatch = users.objects.filter(Q(email = email) & Q(password = password))

        if(len(isMatch) == 1):
            userinfo = users.objects.get(email=email)
            request.session['name'] =userinfo.name
            request.session['email'] = userinfo.email

            return HttpResponseRedirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return HttpResponseRedirect('/user/login/')




#forgot password

class forgotpassword(View):
    @method_decorator(checkingUserAuthentication)
    def get(self, request):
        if(request.isauth):
            return HttpResponseRedirect('/')
        
        else:
            askemail= True
            return render(request,'users/password.html',{'askemail':askemail})
    

    def post(self, request):
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        isverify = users.objects.filter(Q(email = email) & Q(gender = gender))

        if(len(isverify) == 1):
            askemail= False
            return render(request,'users/password.html',{'askemail':askemail, 'email':email}) #this will show the page for  creating new password
        else:
            messages.error(request,'Invalid Credentials')
            return HttpResponseRedirect('/user/forgotpassword/')




class newpassword(View):
   
    def post(self, request,email):

        password = request.POST.get('password')
        cnfpassword = request.POST.get('cnfpassword')

        askemail = False

        if (password == cnfpassword):
            Email = email 
            users.objects.filter(email=Email).update(password=password)
            messages.success(request,'Password has Been Changed...')
            return HttpResponseRedirect('/user/login')
        else:
            messages.error(request,'Password does not matched with cnf password')
            return render(request,'users/password.html',{'askemail':askemail})




#for the profile page and

class dashboard(View):
    @method_decorator(checkingUserAuthentication)
    def get(self, request):
        if (request.isauth):
            username = request.name

            user = users.objects.filter(email = request.email)


            return render(request,'users/dashboard.html',{'username':username,'user':user})
        
        else:
            return HttpResponseRedirect('/user/login/')