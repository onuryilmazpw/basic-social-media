from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feed.models import UserPost

@login_required(login_url='login')
def edit_post(request, id):
    template = "feed/edit_post.html"
    post = UserPost.objects.get(pk=id)
    all_post = [post]
    context = {
        "all_post" : all_post
    }
    return render(request, template, context)