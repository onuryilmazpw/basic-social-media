from django.shortcuts import render

# Create your views here.

def friends_list(request):
    template = "friends/friends_list.html"
    context = {
        
    }
    return render(request, template, context)