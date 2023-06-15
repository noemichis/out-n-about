from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<str:category_name>', views.categories_view, name='categories'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('comment_delete/<int:id>', views.comment_delete, name='comment_delete'),
    path('comment_edit/<int:pk>', views.CommentEdit.as_view(), name='comment_edit'),
]
