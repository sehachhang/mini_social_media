from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

# Home page – show all posts
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# Create a new post
@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user_account = request.user.account  # Get UserAccount from current user
        Post.objects.create(user_account=user_account, title=title, body=body)
        return redirect('home')
    
    return render(request, 'create_post.html')

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