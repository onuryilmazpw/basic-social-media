from django.shortcuts import render
from feed.models import UserPost

# Create your views here.


#UserPost.objects.all().order_by('-post_date')
#if request.GET['q'] and request.GET['q'] is not None:

def index(request):
    template = "core/index.html"
    try:
        q = request.GET['q']
        all_post = UserPost.objects.filter(title__contains=q).order_by('-post_date')
    except:
        all_post = UserPost.objects.all().order_by('-post_date')
    context = {
        "all_post" : all_post
    }
    return render(request, template, context)