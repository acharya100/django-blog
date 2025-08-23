from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.forms import RegisterForm, PostForm
from blog.models import Post
from django.contrib import messages
# Write your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "you have logged in successfully")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "you have logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "please enter valid information")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')

@login_required
def home_view(request):
    posts = list(Post.objects.all())

    def get_created_date(post):
        return post.created_at

    posts.sort(key=get_created_date)

    return render(request, 'home.html', {'posts': posts})

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Post is created")
        return redirect('home')
    return render(request, 'post_form.html', {'form': form, 'title': 'Create Post'})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "You cannot edit the post")
        return redirect('home')
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Post is updated")
        return redirect('home')
    return render(request, 'post_form.html', {'form': form, 'title': 'Edit Post'})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user == post.author:
        post.delete()
        messages.success(request, "Your post has been removed.")
    else:
        messages.error(request, "You cannot delete this post.")

    return redirect('home')

