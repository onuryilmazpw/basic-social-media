from django.shortcuts import render
from feed.models import UserPost

# Create your views here.

def index(request):
    template = "core/index.html"
    context = {
        "all_post" : UserPost.objects.all()
    }
    return render(request, template, context)