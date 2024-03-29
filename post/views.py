from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from post.forms import PostForm, CommentForm
from post.models import Post


def index(request):
    return redirect('/posts')


def posts_list(request):
    query = ''
    if 'query' in request.GET:
        query = request.GET.get('query')
    posts = Post.post_manager.filter(Q(slug__contains=query))
    return render(request, 'posts.html', {
        "posts": posts,
    })


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, created__year=year, created__month=month, created__day=day)
    user = request.user
    comments = post.comments.filter()
    if request.method == 'POST' and 'delete-post' in request.POST:
        post.delete()
        return redirect('/posts')
    elif request.method == 'POST' and 'delete-comment' in request.POST:
        comment = comments.filter(id=request.POST.get('delete-comment', 1))
        comment.delete()
    return render(request, 'post.html', {'post': post, "user": user, 'comments': comments})


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm(data=request.POST)
    if request.method == 'POST' and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect(post)
    return render(request, 'comment_form.html', {'post': post, 'comment_form': comment_form})


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

