from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserPost(models.Model):
    title = models.CharField(max_length=150)
    post_text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    