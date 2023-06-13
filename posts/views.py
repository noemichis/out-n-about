from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Post, Categories, Comment
from .forms import CommentForm


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
    """
    Renders the post details Page
    """
    def get(self, request, slug, *args, **kwargs):
        get_posts = Post.objects.all()
        post = get_object_or_404(get_posts, slug=slug)
        comments = post.comments.filter(approved=True)
        context = {
            'post': post,
            'comments': comments,
            'comment_form': CommentForm(),
        }

        return render(request, 'post_detail.html', context)

    def post(self, request, slug, *args, **kwargs):
        """
        Allows commenting on the posts
        """
        get_posts = Post.objects.all()
        post = get_object_or_404(get_posts, slug=slug)
        comments = post.comments.filter(approved=True)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.related_post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment successfully submitted!')
        else:
            comment_form = CommentForm()

        context = {
            'post': post,
            'comments': comments,
            'comment_form': CommentForm(),
        }

        return render(request, 'post_detail.html', context)
