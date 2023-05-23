from django.contrib import admin
from .models import Post, Categories, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    """
    Add Categories fields to admin panel
    """
    list_display = ['category_name']
    search_fields = ['category_name']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add Post fields to admin panel with Summernote field for content
    """
    list_display = ('title', 'slug', 'status', 'date_posted', 'category')
    search_fields = ['title', 'content', 'category']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_posted')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add Comments field to admin panel
    """
    list_display = ('author', 'related_post', 'body', 'comment_on', 'approved')
    search_fields = ['author', 'body']
    list_filter = ('approved', 'comment_on')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
