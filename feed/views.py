from django.shortcuts import render
from .models import UserPost

# Create your views here.

def add_post(request):
    template = "feed/add_post.html"
    user = request.user

    context = {
        "bilgi" : ""
    }
    if request.method == "POST":
        title = request.POST["title"]
        post_text = request.POST["post_text"]

        UserPost.objects.create(title=title, post_text=post_text, owner=user)

        context["post_text"] = post_text
        context["title"] = title


    return render(request, template, context)