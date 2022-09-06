from django.shortcuts import render
from users.middleware import checkingUserAuthentication
from django.utils.decorators import method_decorator
# Create your views here.

@(checkingUserAuthentication)
def index(request):
    if(request.isauth):
        return render(request,'home/welcome.html',{'username':
        request.name})
    else:
        return render(request,'home/home.html')