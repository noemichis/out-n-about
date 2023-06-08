from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<str:category_name>', views.categories_view, name='categories'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    # path('categories/', views.category_posts, name='categories')
]
