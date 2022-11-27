from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from account.forms import LoginUserForm

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    template = "account/login.html"

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Başarılı bir şekilde giriş yaptınız.")
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