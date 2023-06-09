from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Categories


def index(request):
    get_posts = Post.objects.all()
    context = {
        'post_list': get_posts
    }

    return render(request, 'index.html', context)


def categories_view(request, category_name):
    selected_category = Categories.objects.get(category_name=category_name)
    categories_post = Post.objects.filter(
        category=selected_category
        )
    context = {
        'selected_category': selected_category,
        'posts': categories_post
    }

    return render(request, 'categories.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        get_posts = Post.objects.all()
        post = get_object_or_404(get_posts, slug=slug)
        context = {
            'post': post,
        }

        return render(request, 'post_detail.html', context)
