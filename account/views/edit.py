from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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