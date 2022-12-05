from django.db import models
from account.models import CustomUserModel

class Profile(models.Model):
    about = models.CharField(max_length=250)
    account = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Profiller"
        verbose_name = "Profil"