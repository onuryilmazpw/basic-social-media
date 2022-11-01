from django.shortcuts import render, redirect
from feed.models import UserPost

# Create your views here.

def user_profile(request):
    template = "userprofile/profile.html"
    if not request.user.is_authenticated:
        return redirect("home")

    context = {
        "all_post" : UserPost.objects.filter(owner=request.user).order_by('-post_date')
    }
    return render(request, template, context)

def profile_edit(request):
    template = "userprofile/profile_edit.html"
    context = {
        
    }
    return render(request, template, context)