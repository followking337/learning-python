from pages.models import Page


def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    # list with elements object Page, within each one there is tuple with object attributes
    # pages = Page.objects.values_list('title', flat=True)  # plain text
    # pages = Page.objects.all()  # it will return all objects with all info (complete info)
    return {
        'pages': pages
    }
