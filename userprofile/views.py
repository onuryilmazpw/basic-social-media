from django.shortcuts import render
from feed.models import UserPost

# Create your views here.

def user_profile(request):
    template = "userprofile/profile.html"
    context = {
        "all_post" : UserPost.objects.filter(owner=request.user)
    }
    return render(request, template, context)

def profile_edit(request):
    template = "userprofile/profile-edit.html"
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