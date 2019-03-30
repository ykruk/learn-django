from django import forms
from django.forms import ModelForm
from .models import Post, Exposition, Message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'photo')

class ExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ('title', 'description', 'add_text', 'photo')

# class ContactForm(forms.Form):
#     name = forms.CharField(label='Имя')
#     email = forms.EmailField(label='Email', required=False)
#     message = forms.CharField(label='Сообщение', widget=forms.Textarea)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('sender_name', 'sender', 'message')

        