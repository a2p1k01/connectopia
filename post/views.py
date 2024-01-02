from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from post.forms import PostForm, LoginForm, RegistrationForm
from post.models import Post


def index(request):
    return redirect('/posts')


def profile(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    if user.is_authenticated:
        return render(request, 'profile.html', {"user": user})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/login')
    form = RegistrationForm()
    return render(request, 'register.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/posts')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def posts_list(request):
    posts = Post.post_manager.filter()
    return render(request, 'posts.html', {"posts": posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, created__year=year, created__month=month, created__day=day)
    user = request.user
    if request.method == 'POST':
        post.delete()
        return redirect('/posts')
    return render(request, 'post.html', {'post': post, "user": user})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if post_form.is_valid():
            post_form.save(commit=False)
            post.save()
            post_form.save_m2m()
            return redirect('/posts')
    return render(request, 'edit_post.html',
                  {'post_form': post_form, 'post': post}
                  )


def new_post(request):
    post = None
    post_form = PostForm(data=request.POST, files=request.FILES)
    if post_form.is_valid() and request.method == 'POST':
        post = post_form.save(commit=False)
        post.author = request.user
        post.save()
        post_form.save_m2m()
        return redirect('/posts')
    return render(request, 'new_post.html',
                  {'post_form': post_form, 'post': post}
                  )

