from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Exposition, Post_img, Exposition_img, Message
from .forms import PostForm, ExpositionForm, MessageForm

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()[0:4]
    expositions = Exposition.objects.all()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('/feedback.html')
    else:
        form = MessageForm()
    return render(request, 'museum/home.html', {
    'posts': posts,
    'expositions': expositions,
    'form': form
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_imgs = Post_img.objects.filter(post=post.id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('/feedback.html')
    else:
        form = MessageForm()
    return render(request, 'museum/post_detail.html', {
        'post': post,
        'form': form})

def exposition_detail(request, pk):
    exposition = get_object_or_404(Exposition, pk=pk)
    exp_imgs = Exposition_img.objects.filter(exp=exposition.id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('/feedback.html')
    else:
        form = MessageForm()
    return render(request, 'museum/exposition_detail.html', {
    'exposition': exposition,
    'exp_imgs': exp_imgs,
    'form': form}) 

def news(request):
    news = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('/feedback.html')
    else:
        form = MessageForm()
    return render(request, 'museum/news.html', {
    'news': news,
    'form': form})

def feedback(request):
    return render(request, 'museum/feedback.html', {})

def about(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('/feedback.html')
    else:
        form = MessageForm()
    return render(request, 'museum/about.html', {
    'form': form
    })

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             if 'photo' in request.FILES:
#                 form.photo = request.FILES['photo']
#             form.save(commit=True)
#             return HttpResponse('image upload success')

#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'museum/post_edit.html', {'form': form}) 

# def exposition_edit(request):
#     form = ExpositionForm()
#     if request.method == 'POST':
#         form =ExpositionForm(request.POST, request.FILES)
#         if form.is_valid():
#             if 'photo' in request.FILES:
#                 form.photo = request.FILES['photo']
#             form.save(commit=True)
#             return HttpResponse('image upload success')
#         else:
#             print(form.errors)
#         return render(request, 'museum/exposition_edit.html', {'form': form})