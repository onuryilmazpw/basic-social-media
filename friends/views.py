from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def friends_list(request):
    template = "friends/friends_list.html"
    context = {
        
    }
    return render(request, template, context)