from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm



from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages

# Create your views here.

def loginUser(request):

    form = LoginForm(request.POST or None)
    
    context = {"form":form}
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola hatalı...")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız...")
        login(request,user)
        return redirect("index")
    return render (request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı...")
    return redirect("index")
