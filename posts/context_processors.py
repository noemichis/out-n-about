"""
Context processors
"""

from .models import Categories


def categories_list(request):
    """
    Creates context for categories so it can be used across all pages
    """
    categories_list = Categories.objects.all()
    context = {
        'categories_list': categories_list,
    }

    return context
