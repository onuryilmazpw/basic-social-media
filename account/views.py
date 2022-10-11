from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    template = "account/login.html"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context = {
                "error": "Kullanıcı adı veya parola yanlış"
            }
            return render(request, template, context)
    else:
        return render(request, template)

def register_request(request):
    pass

def logout_request(request):
    pass