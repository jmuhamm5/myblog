from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)

    page = request.GET.get('page')
    categories = Category.list_categories()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'pages/home.html', {'posts': posts, 'categories': categories})


def single(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pages/single.html', {'post': post})

def archive(request, category):
    cat = Category.objects.get(slug=category)
    post_list = Post.objects.filter(category__pk=cat.id)
    paginator = Paginator(post_list, 3)

    page = request.GET.get('page')
    categories = Category.list_categories()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'pages/archive.html', {'posts': posts, 'categories': categories, 'category': cat.title})