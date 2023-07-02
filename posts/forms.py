"""
Forms
"""

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for the Post Comments
    """
    class Meta:
        model = Comment
        fields = ('body', )
