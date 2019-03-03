from django import forms

from .models import Post, Exposition

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'photo')

class ExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ('title', 'description', 'add_text', 'photo')