from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from feed.forms import UserPostForm

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
            messages.success(request, "Yeni gönderi oluşturuldu.")
            return redirect("profile")
    else:
        form = UserPostForm()
    context = {
    "form" : form
    }
    return render(request, template, context)