from django import forms
from .models import UserPost

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('title', 'post_text',)
        labels = {
            "title" : "Gönderi Başlığı",
            "post_text" : "Gönderi İçeriği"
        }
