"""
Views for Posts and comments
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import CommentForm


class Index(generic.ListView):
    """
    Renders the index page
    """
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'


def about(request):
    """
    Renders the about page
    """
    return render(request, 'about.html')


def categories_view(request, category_name):
    """
    Creates the categories objects
    and renders them to selected pages
    """
    selected_category = Categories.objects.get(category_name=category_name)
    categories_post = Post.objects.filter(
        category=selected_category
        )
    context = {
        'selected_category': selected_category,
        'posts': categories_post
    }

    return render(request, 'categories.html', context)


class PostDetail(View, SuccessMessageMixin):
    """
    Renders the post details Page
    """
    def get(self, request, slug, *args, **kwargs):
        get_posts = Post.objects.all()
        post = get_object_or_404(get_posts, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            'post': post,
            'comments': comments,
            'liked': liked,
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
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = {
            'post': post,
            'comments': comments,
            'liked': liked,
            'comment_form': comment_form,
        }

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.related_post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment successfully submitted!')

            return redirect(reverse('post_detail', args=(post.slug,)))
        else:
            comment_form = CommentForm()

        return render(request, 'post_detail.html', context)


@login_required
def comment_delete(request, id):
    """
    Allows users to delete their own comments
    """
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    messages.success(request, 'Comment successfully deleted')

    return redirect('post_detail', slug=comment.related_post.slug)


class CommentEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Allows users to edit and update their comments
    """
    model = Comment
    template_name = 'comment_edit.html'
    form_class = CommentForm
    success_message = "Comment successfully updated"


class PostLike(LoginRequiredMixin, View):
    """
    Allows users to like and unlike posts
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'Post unliked')

        else:
            post.likes.add(request.user)
            messages.success(request, 'Post successfully liked')

        return redirect('post_detail', slug=post.slug)
