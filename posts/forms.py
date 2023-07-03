"""
Forms
"""

from .models import Comment, Contact
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for the Post Comments
    """
    class Meta:
        model = Comment
        fields = ('body', )
        labels = {'body': 'Leave a comment'}


class ContactForm(forms.ModelForm):
    """
    Form for the Contact Us page
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
