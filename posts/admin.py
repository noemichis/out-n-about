from django.contrib import admin
from .models import Post, Categories, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    """
    Add Categories fields to admin panel
    """


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add Post fields to admin panel with summernote field for content
    """
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add Comments field to admin panel
    """
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
