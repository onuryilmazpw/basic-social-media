from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.user_profile, name="profile"),
]