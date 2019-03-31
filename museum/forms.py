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

class MessageForm(forms.ModelForm):
    sender_name = forms.CharField(widget=forms.TextInput(attrs={
        'name':'name',
        'class':'form-control',
        'id':'name',
        'placeholder':'Имя'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={
        'name':'email',
        'class':'form-control',
        'id':'email',
        'placeholder':'Email'}))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'name':'message',
        'class':'form-control',
        'id':'mes',
        'rows':'4',
        'placeholder':'Сообщение'}))
    class Meta:
        model = Message
        fields = ('sender_name', 'sender', 'message', 'reply')

        