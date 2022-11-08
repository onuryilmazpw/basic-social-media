from django import forms
from django.forms import widgets
from .models import UserPost

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('title', 'post_text',)
        labels = {
            "title" : "Gönderi Başlığı",
            "post_text" : "Gönderi İçeriği"
        }
        widgets = {
            "title" : widgets.TextInput(attrs={"class":"form-control"}),
            "post_text" : widgets.Textarea(attrs={"class":"form-control", "rows":"5"})
        }
