from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from feed.models import UserPost

@login_required(login_url='login')
def user_profile(request):
    template = "userprofile/profile.html"

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