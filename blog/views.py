from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Post

def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})

def index(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('index', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'index.html', {'post': post, 'form': form})