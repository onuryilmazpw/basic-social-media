from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserPostForm

# Create your views here.

@login_required(login_url='login')
def add_post(request):
    template = "feed/add_post.html"
    user = request.user

    if request.method == "POST":
        form = UserPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = user
            post.save()
            return redirect("profile")
    else:
        form = UserPostForm()
    context = {
    "form" : form
    }
    return render(request, template, context)