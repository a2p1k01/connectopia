from django.shortcuts import render, redirect, get_object_or_404

from post.forms import PostForm
from post.models import Post


def index(request):
    return redirect('/posts')


def posts_list(request):
    posts = Post.post_manager.filter()
    return render(request, 'posts.html', {"posts": posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, created__year=year, created__month=month, created__day=day)
    return render(request, 'post.html', {'post': post})


def new_post(request):
    post = None
    post_form = PostForm(data=request.POST)
    if post_form.is_valid() and request.method == 'POST':
        post = post_form.save(commit=False)
        post.author = request.user
        post.save()
    return render(request, 'new_post.html',
                  {'post_form': post_form, 'post': post})
