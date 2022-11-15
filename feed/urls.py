from django.urls import path
from . import views

urlpatterns = [
    path("add-post/", views.add_post, name="add_post"),
]