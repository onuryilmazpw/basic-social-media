from django.shortcuts import render

# Create your views here.

def index(request):
    template = "core/index.html"
    context = {
        "deneme" : "deneme"
    }
    return render(request, template, context)