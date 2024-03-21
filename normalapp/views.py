from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
def register(request):
    return render(request,"register.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser=User.objects.create_user(username,email,password1)
        myuser.save()
        messages.success(request,"your account was created")
        return redirect('signin')

    else:
        return render(request,"signup.html")


def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        myuseraccount=authenticate(username=username,password=password)
        if myuseraccount is not None:
            login(request,myuseraccount)
            return redirect('commerce')
            
        else:
            messages.error(request,'invalid credential')
            return redirect('signin')

    else:
        return render(request,"login.html")

def commerce(request):
    return render(request,"index.html")

def signout(request):
    logout(request)
    return render(request,"home.html")
    return redirect('signin')

def feedback(request):
    return render(request,'feedback.html')
