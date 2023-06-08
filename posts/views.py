from django.shortcuts import render
from django.views import generic
from .models import Post, Categories


def index(request):
    get_cats = Categories.objects.all()
    get_posts = Post.objects.all()
    context = {
        'categories_list': get_cats,
        'post_list': get_posts
    }

    return render(request, 'index.html', context)


def categories_view(request, category_name):
    categories = Categories.objects.all()
    selected_category = Categories.objects.get(category_name=category_name)
    categories_post = Post.objects.filter(
        category=selected_category
        )
    context = {
        'categories_list': categories,
        'selected_category': selected_category,
        'posts': categories_post
    }

    return render(request, 'categories.html', context)
