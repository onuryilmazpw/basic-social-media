from django.shortcuts import redirect, render
from account.models import CustomUserModel

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
        elif CustomUserModel.objects.filter(username=username).exists():
            context["error"] = "Bu kullanıcı adı daha önce alınmış."
            return render(request, template, context)
        elif CustomUserModel.objects.filter(email=email).exists():
            context["error"] = "Bu e-posta başka bir üyeşiğe ait."
            return render(request, template, context)
        else:
            user = CustomUserModel.objects.create_user(username=username,
                                            email=email, 
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password)
            user.save()
            return redirect("login")
    else:
        return render(request, template)