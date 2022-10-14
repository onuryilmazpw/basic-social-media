from django.shortcuts import render

# Create your views here.

def add_post(request):
    template = "feed/add_post.html"
    context = {
        
    }
    return render(request, template, context)