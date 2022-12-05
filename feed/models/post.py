from django.db import models
from account.models import CustomUserModel
from django.utils import timezone

class UserPost(models.Model):
    title = models.CharField(max_length=150)
    post_text = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Gönderiler"
        verbose_name = "Gönderi"

    def __str__(self):
        return self.title