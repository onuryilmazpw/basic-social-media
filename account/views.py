from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from account.forms import LoginUserForm

# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    template = "account/login.html"

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                nextUrl = request.GET.get('next')
                if nextUrl is None:
                    return redirect('home')
                else:
                    return redirect(nextUrl)
            else:
                context= {'form':form}
                return render(request, template, context)
        else:
            context= {'form':form}
            return render(request, template, context)
    else:
        form = LoginUserForm()
        context= {'form':form}
        return render(request, template, context)

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

@login_required(login_url='/login')
def account_edit(request):
    template = "account/account_edit.html"
    user = request.user
    context = {
        "bilgi" : "Bilgilerde değişiklik yok!"
    }
    if request.method == "POST":
        if user.username != request.POST["username"]:
            user.username = request.POST["username"]
            context["bilgi"] = "Bilgiler güncellendi"

        if user.email != request.POST["email"]:
            user.email = request.POST["email"]
            context["bilgi"] = "Bilgiler güncellendi"
        
        if user.first_name != request.POST["firstname"]:
            user.first_name = request.POST["firstname"]
            context["bilgi"] = "Bilgiler güncellendi"
    
        if user.last_name != request.POST["lastname"]:
            user.last_name = request.POST["lastname"]
            context["bilgi"] = "Bilgiler güncellendi"
        
        user.save()
    else:
        context["bilgi"] = "Değiştirmek istediğiniz bilgileri düzenleyip Kaydet butonuna basın."

    context["username"] = user.username
    context["email"] = user.email
    context["firstname"] = user.first_name
    context["lastname"] = user.last_name

    return render(request, template, context)