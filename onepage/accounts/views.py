from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
                user.save()
                print('User Created')
        else:
            print('password not matched')
            messages.info(request, 'Password not matched')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Not a user')
            return  redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')