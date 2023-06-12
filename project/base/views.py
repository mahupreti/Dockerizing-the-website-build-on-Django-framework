# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello Sir, This is running three different services: nginx, django-app, and postgresql!")

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm,messageForm
from .models import Post, Category, Message

def home(request):

    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')  # posts = .posts.filter(status=Post.ACTIVE)

    # return render(request, 'base/category.html', {'category': category, 'posts': posts})

    return render(request, 'base/home.html', { 'posts': posts}) 


def contact(request):
    return render(request, 'base/contact.html')


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'base/detail.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'base/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'base/search.html', {'posts': posts, 'query': query})

def blog(request):

    posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')  # posts = .posts.filter(status=Post.ACTIVE)

    # return render(request, 'base/category.html', {'category': category, 'posts': posts})

    return render(request, 'base/blogHome.html', { 'posts': posts}) 


def message(request):
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():

            message = form.cleaned_data['message']
            message = Message(message=message)
            message.save()
            return redirect('home')
        
    else:
        form= messageForm()

    return render(request, 'base/contact.html', {'form': form})