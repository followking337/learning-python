from blog.models import Category, Article


def get_categories(request):
    categories_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_use).values_list('id', 'name')  # sub-consult

    return {
        'categories': categories,
        'ids': categories_use
    }
