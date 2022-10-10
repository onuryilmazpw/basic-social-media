from django.shortcuts import render

# Create your views here.

def user_profile(request):
    template = "userprofile/profile.html"
    context = {
        
    }
    return render(request, template, context)