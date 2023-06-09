from .models import Categories


def categories_list(request):
    categories_list = Categories.objects.all()
    context = {
        'categories_list': categories_list,
    }

    return context
