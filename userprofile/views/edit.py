from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile_edit(request):
    template = "userprofile/profile_edit.html"
    context = {
        
    }
    return render(request, template, context)