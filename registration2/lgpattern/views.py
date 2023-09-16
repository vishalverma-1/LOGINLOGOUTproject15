#-----------USER REGISTRATION FORM----------
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import vishal
from django.contrib.auth.models import auth
def myfun(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        obj=vishal.objects.create(name=name,mobile=mobile,password=password)
        if password==confirm_password:
            obj.save()
            return redirect('login')
        else:
            return HttpResponse("INVALID CREDENTIALS")
    else:
            
        return render(request,'verma.html')
        

 #-----------LOGIN PAGE---------------   

def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        data=vishal.objects.get(name=name,password=password)
        if (data is not None):
            return redirect('website')
        
    else:
        return render(request,'login.html')
            
def home(request):
    return render(request,'website.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
