from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import users,posts,activity,post_activities
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
        #img tag nam attr wala hai input tag ka <imput name=img type=file>
        if 'img' in request.FILES:
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

            mypost = posts.objects.filter(user=users.objects.get(email=request.email))

            follow = activity.objects.filter(whofollow= users.objects.get(email=request.email))

            followers= activity.objects.filter(whomtofollow= users.objects.get(email=request.email))

            return render(request,'users/dashboard.html',{'username':username,'user':user,'total' : len(mypost),'follow' : len(follow),'followers':len(followers)})
        
        else:
            return HttpResponseRedirect('/user/login/')



#for editing the information about

class editinfo(View):
    
    def get(self, request,id):
        if 'email' in request.session:
            user = users.objects.get(id=id)

            if user.email == request.email:
                return render(request,'users/edit.html',{'username':request.name,'user':user})
            else:
                return HttpResponse('Invalid request')

            
        else:
            return HttpResponseRedirect('/user/login')

    
    def post(self, request,id):
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')

        if len(name) <= 2:
            messages.info(request,'Name is too short')
            return HttpResponseRedirect(f'/user/editinfo/{id}/')
        else:
            newName = name
            users.objects.filter(id=id).update(name=newName)
            request.session['name'] = newName
        
        #checking email
        
        if request.session['email'] != email:
            user = users.objects.filter(email = email)

            if(len(user) >= 1):
                messages.info(request,'Email Already Exist')
                return HttpResponseRedirect(f'/user/editinfo/{id}')
            else:
                newEmail = email
                users.objects.filter(id=id).update(email=newEmail)
                request.session['email'] = email
               
        else:
            pass
            
            

        
        if password == "":
            pass
        else:
            if len(password) < 3:
                messages.info(request,'Password is too small')
                return HttpResponseRedirect(f'/user/editinfo/{id}')
            else:
                users.objects.filter(id=id).update(password=password)

        
        users.objects.filter(id=id).update(gender = gender,address = address)

        return HttpResponseRedirect(f'/user/dashboard/')




class editimg(View):
    def get(self, request,id):
        user = users.objects.get(id=id)

        if user.email == request.session['email']:
            return render(request,'users/editpic.html',{'username':user.name,'user':user})
        else:
            return HttpResponseRedirect(f'/user/login')
    
    def post(self, request,id):
        user = users.objects.get(id=id)

        if user.email == request.session['email']:

            userimage = request.FILES['img']


            userimg = 'userimg/'+ str(userimage)

           
            users.objects.filter(id=id).update( userimg =  userimg)

            return HttpResponseRedirect('/user/dashboard/')
        else:
            return HttpResponseRedirect(f'/user/login')





#remove image and set default image provide by bookmarks

class rmvimg(View):
    def get(self, request,id):
        user = users.objects.get(id=id)

        if user.email == request.session['email']:

            users.objects.filter(id=id).update( userimg = False)
           
            return HttpResponseRedirect('/user/dashboard/')
        else:
            return HttpResponseRedirect(f'/user/login')

        



#post users.objects.

class post(View):
    @method_decorator(checkingUserAuthentication)
    def get(self, request):
        if request.isauth:

            mypost = posts.objects.filter(user=users.objects.get(email=request.email))



            return render(request, 'users/post.html',{
                'username' : request.name,
                'post' : mypost,
                'total' : len(mypost)
            }) 
        else:
            return HttpResponseRedirect('/user/login')
    
    def post(self, request):

        postdata = request.POST.get('postdata')
        
        
        if 'postimg' in request.FILES:
            img = request.FILES['postimg']
        else:
            img = False
      

       
        if postdata == '':
            messages.info(request,'Please write something in the text box ')
            return HttpResponseRedirect('/user/post/')
        else:
            
            posts.objects.create(postdata=postdata,postimg=img,user=users.objects.get(email=request.email))

            return HttpResponseRedirect('/user/post/')




#for the deleteing post data
class deleteethispost(View):
    
    def get(self, request,id):
        if 'email' in request.session:
            email = request.session['email']

            isexist  = users.objects.filter(email=email).exists()

            if isexist:
                posts.objects.get(id=id).delete()
                return HttpResponseRedirect('/user/post/')
            else:
                return HttpResponse('Invalid Request')

        else:
            return HttpResponseRedirect('/user/login')




#for the follwing person who


class people(View):
    @method_decorator(checkingUserAuthentication)
    def get(self, request):
        if request.isauth:
            people = users.objects.all() 

            #now we will send for the followers list and

            act = activity.objects.filter(whofollow = users.objects.get(email=request.email))
            
            return render(request,'users/people.html',{'people':people ,'username':request.name,
            'len' : len(people),'act':act})
        else:
            return HttpResponseRedirect('/user/login/')




#for showinf the individuals profile page

class profile(View):
    def get(self, request,id):

        if 'email' in request.session:
            isexist = users.objects.filter(email = request.session['email']).exists()
            if isexist:
                username = request.session['name']

                isfollow = activity.objects.filter(Q(whofollow= users.objects.get(email= request.session['email'])) & Q(whomtofollow= users.objects.get(id=id))).exists()

                
            else:
                username = False
                isfollow = False

        else:
            username = False
            isfollow = False

        
        isUser = users.objects.filter(id=id).exists()

        if isUser:

            user = users.objects.filter(id=id)
            totalpost = posts.objects.filter(user = users.objects.get(id=id))
            totalfollowing = len(activity.objects.filter(whofollow= users.objects.get(id=id)))
            totalfollower = len(activity.objects.filter(whomtofollow=users.objects.get(id=id)))


            #to check weather the loged in user follow this guy or not 



            return render(request, 'users/profile.html',{'username':username,'user':user,'total' :len(totalpost),'totalfollowing':totalfollowing,'totalfollower':totalfollower,'id':id,'isfollow':isfollow,
            'post':totalpost})
            
        else:
            return HttpResponse('Invalid Request..')

        
        

#follow user

class follow(View):
    def get(self, request,id):
        #first we need to follow
        if 'email' in request.session:
            if 'name' in request.session:
                isexist = users.objects.filter(Q(email = request.session['email']) & Q(name = request.session['name'])).exists()

                if isexist:

                    #if user is aurthorised then we need to follower id is exist or not exist

                    sameperson = users.objects.filter(Q(id=id) & Q(email = request.session['email']) & Q(name = request.session['name'])).exists()

                    if sameperson:
                        return HttpResponse('Cannot follow yourself..')

                    isPerson = users.objects.filter(id=id).exists() 
                    
                
                    if isPerson:

                        #now we will check user is alredy follow or not 
                        
                        isfollow = activity.objects.filter(Q(whomtofollow = users.objects.get(id=id)) & Q(whofollow = users.objects.get(email = request.session['email']))).exists()

                        if isfollow:
                            return HttpResponse('You are alredy following this users..')
                        
                        else:

                            activity.objects.create(whofollow=users.objects.get(email = request.session['email']),whomtofollow = users.objects.get(id=id)) 

                            return HttpResponseRedirect('/user/people/')


                    else:
                        return HttpResponse('User does not exist or deleted the account..')

                  
                else:
                    return HttpResponseRedirect('/user/login')

            
            else:
                return HttpResponseRedirect('/user/login')

        else:
            return HttpResponseRedirect('/user/login')




#for unfollow user

class unfollow(View):
    def get(self, request, id):
        if 'email' in request.session:
            if 'name' in request.session:
                isexist = activity.objects.filter(Q(whomtofollow= users.objects.get(id=id)) & Q(whofollow= users.objects.get(email= request.session['email']))).exists()

                if isexist:
                    activity.objects.filter(Q(whomtofollow= users.objects.get(id=id)) & Q(whofollow= users.objects.get(email= request.session['email']))).delete()
                    return HttpResponseRedirect('/user/people/')
                else:
                    return HttpResponse('User does not exsist')
            else:
                return HttpResponseRedirect('/user/login')
        else:
            return HttpResponseRedirect('/user/login')
        

#see the followlist for more information

class followlist(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            follow = activity.objects.filter(whofollow= users.objects.get(email=request.email))
            return render(request, 'users/follow.html',{
                'username': request.name
                ,'follow': follow,
                'len' : len(follow)
            })
        else:
            return HttpResponseRedirect('/user/login')



class followerlist(View):
    @method_decorator(checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            follower = activity.objects.filter(whomtofollow= users.objects.get(email=request.email))
            return render(request, 'users/follower.html',{
                'username': request.name
                ,'follower': follower,
                'len' : len(follower)
            })
        else:
            return HttpResponseRedirect('/user/login')



#post activity activity
class post_activity(View):
    def get(self, request,id,uid):
        if 'email' in request.session:
            if 'name' in request.session:
                post = posts.objects.filter(id=id)
                username = request.session['name']

                #check user exist or not

                isuser = users.objects.filter(id=uid).exists()

                if isuser == False:
                    return HttpResponse('Invalid request')


                if post.exists():

                    #and check user follow or not or post is of user or someone else 

                    postbelong = posts.objects.filter(Q(user = users.objects.get(email = request.session['email'])) & Q(id=id))

                    if postbelong.exists():
                        #it means post is of user itself
                        isfollow =True
                        
                    
                    else:
                        #if this post does not belong to user then check user follow that person or not  
                        isfollow = activity.objects.filter(Q(whofollow = users.objects.get(email = request.session['email'])) & Q(whomtofollow= users.objects.get(id=uid))).exists()

                    #checking comments on that post     

                    postcomments = post_activities.objects.filter(post = posts.objects.get(id=id))
              
                    return render(request, 'users/post_act.html',{
                        'username':username,'post':post ,'isfollow':isfollow,
                        'cmt':postcomments})
                else:
                    return HttpResponse('Post dose not exist')
                
            else:
                return HttpResponseRedirect('/user/login/')
        else:
            return HttpResponseRedirect('/user/login/')
    

    def post(self, request,id,uid):
        cmt = request.POST.get('comment')

        if cmt.strip() == '':
            messages.info(request,'You should write somthing in comment box..')
            
        else:

            post_activities.objects.create(user = users.objects.get(email = request.session['email']),post = posts.objects.get(id=id),comments = cmt)
        
        return HttpResponseRedirect(f'/user/post_activity/{id}/{uid}/')