from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.user_profile, name="profile"),
    path("profile/edit", views.profile_edit, name="profile_edit"),
]