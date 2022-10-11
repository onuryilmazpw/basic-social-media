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
    if request.user.is_authenticated:
        return redirect("home")

    template = "account/register.html"

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        context = {
                    "username" : username,
                    "email" : email,
                    "firstname" : firstname,
                    "lastname" : lastname
                }

        if password != repassword:
            context["error"] = "Parola Eşleşmiyor"
            return render(request, template, context)
        elif User.objects.filter(username=username).exists():
            context["error"] = "Bu kullanıcı adı daha önce alınmış."
            return render(request, template, context)
        elif User.objects.filter(email=email).exists():
            context["error"] = "Bu e-posta başka bir üyeşiğe ait."
            return render(request, template, context)
        else:
            user = User.objects.create_user(username=username,
                                            email=email, 
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password)
            user.save()
            return redirect("login")
    else:
        return render(request, template)

def logout_request(request):
    logout(request)
    return redirect("home")