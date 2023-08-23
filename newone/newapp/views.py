from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        email=request.POST['email']
        ps=request.POST['password']
        cps=request.POST['password1']

        if ps==cps:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=fn, last_name=ln, email=email, password=ps)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request, "Passwords are does not match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        ps = request.POST['password']
        user=auth.authenticate(username=username,password=ps)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request, "login.html")