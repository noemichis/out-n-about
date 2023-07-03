"""
Models for the posts
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Categories(models.Model):
    """
    Model for Categories
    """
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    """
    Model for Post
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_summary = models.TextField()
    content = models.TextField()
    post_image = CloudinaryField('image', default='placeholder')
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    comment_number = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def likes_number(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for Comment
    """
    related_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    comment_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['comment_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author.username}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.related_post.slug])


class Contact(models.Model):
    """
    Model for Contacting
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
