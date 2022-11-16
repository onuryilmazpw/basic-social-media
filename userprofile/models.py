from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    about = models.CharField(max_length=250)
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)