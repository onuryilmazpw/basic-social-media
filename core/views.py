from django.shortcuts import render
from feed.models import UserPost

# Create your views here.

def index(request):
    template = "core/index.html"

    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        all_post = UserPost.objects.filter(title__contains=q).order_by('-post_date')
    else:
        all_post = UserPost.objects.all().order_by('-post_date')
        
    context = {
        "all_post" : all_post
    }
    return render(request, template, context)