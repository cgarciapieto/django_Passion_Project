from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        labels = {'title': 'username', 'content': "",'dateCreated': 'Date' }
        exclude = ['id']