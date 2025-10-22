from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from main.forms import personform
from main.models import profile
# Create your views here.

def home(request):
    data=profile.objects.all()
    return render(request,"home.html",{'data':data})

def edit(request,pk):
    instance=profile.objects.get(pk=pk)
    if request.method == 'POST':
        
        frm = personform(request.POST,instance=instance)
        if frm.is_valid():
            frm.save()
            return redirect("home")
    else:
        frm = personform(instance=instance)
        
    return render(request,"add.html",{'frm':frm})

def delete(request,pk):
    instance=profile.objects.get(pk=pk)
    instance.delete()
    return redirect("home")



def add(request):
    if request.method == 'POST':
        frm=personform(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect("home")
    else:
        frm=personform()

    return render(request,"add.html",{'frm':frm})

def signup_view(request):
    error=None
    user=None
    if request.method == "POST":
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            user=User.objects.create_user(username=username,password=password)
            if user:
                return redirect('login_view')
        except Exception as e:
            error=str(e)

    return render(request,"signup.html",{'error':error})

def login_view(request):
    user=None
    error=None
    if request.method == "POST":
       
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error="invalid credentials"
    return render(request,"login.html",{'error':error})

def logout_view(request):
    logout(request)
    return redirect("login_view")