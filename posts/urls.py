from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<str:category_name>', views.categories_view, name='categories'),
    # path('categories/', views.category_posts, name='categories')
]
