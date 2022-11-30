from django.shortcuts import render,redirect
from .forms import RegisterForm ,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
# Create your views here.

def logoutuser(request):
    logout(request)
    return redirect("index")


def register(request):
    form =RegisterForm(request.POST or None)

    context ={
        "form":form
    }
    if form.is_valid():
        username =form.cleaned_data.get("username")
        password =form.cleaned_data.get("password")

        
        yeniK= User(username=username)
        yeniK.set_password(password)

        yeniK.save()

        login(request, yeniK)
        messages.success(request, "HG Reizzzz. Kayıt Tamamlandır Şimdi Giriş Yapabilirsin...")

        return redirect("index")


    

    return render(request, "register.html",context)


def userlogin(request):
    form =LoginForm(request.POST or None)

    context ={
        "form":form
    }
    
    if form.is_valid():
        username =form.cleaned_data.get("username")
        password =form.cleaned_data.get("password")

        Kullanıcı =authenticate(username=username,password=password)

        if Kullanıcı is None:
            messages.success(request,"Kankam şifre veya isim hatalı ama hangisi söylemem :)")
            return redirect("/user/userlogin")
        login(request, Kullanıcı)
        messages.success(request, "Hoşgeldin kankaa......")

        return redirect("index")

    return render(request, "userlogin.html",context)