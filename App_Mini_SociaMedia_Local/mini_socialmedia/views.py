from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

# Home page – show all posts and allow creating new post inline
@login_required
def home(request):
    posts = Post.objects.all().order_by('-id')  # newest first

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body:
            user_account = request.user.account
            Post.objects.create(user_account=user_account, title=title, body=body)
            return redirect('home')

    return render(request, 'home.html', {'posts': posts})

# Add a comment to a post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        description = request.POST.get('description')
        user_account = request.user.account
        Comment.objects.create(post=post, user_account=user_account, description=description)
        return redirect('home')

    return render(request, 'add_comment.html', {'post': post})