from django.urls import path
from . import views

urlpatterns = [
    path("friends-list/", views.friends_list, name="friends_list"),
]