from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Exposition
from .forms import PostForm, ExpositionForm

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    expositions = Exposition.objects.all()
    return render(request, 'museum/home.html', {
    'posts': posts,
    'expositions': expositions
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'museum/post_detail.html', {'post': post})

def exposition_detail(request, pk):
    exposition = get_object_or_404(Exposition, pk=pk)
    return render(request, 'museum/exposition_detail.html', {'exposition': exposition}) 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'museum/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            return HttpResponse('image upload success')

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'museum/post_edit.html', {'form': form}) 

def exposition_edit(request):
    form = ExpositionForm()
    if request.method == 'POST':
        form =ExpositionForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            return HttpResponse('image upload success')
        else:
            print(form.errors)
        return render(request, 'museum/exposition_edit.html', {'form': form})