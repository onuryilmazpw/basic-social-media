from django.shortcuts import render, redirect
from django.db.models import Q
from feed.models import UserPost

# Create your views here.

def user_profile(request):
    template = "userprofile/profile.html"
    if not request.user.is_authenticated:
        return redirect("login")

    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        all_post = UserPost.objects.filter(
            Q(owner=request.user) & 
            (Q(title__contains=q) | Q(post_text__contains=q))
        ).order_by('-post_date')
    else:
        all_post = UserPost.objects.filter(owner=request.user).order_by('-post_date')


    context = {
        "all_post" : all_post
    }
    return render(request, template, context)

def profile_edit(request):
    template = "userprofile/profile_edit.html"
    context = {
        
    }
    return render(request, template, context)