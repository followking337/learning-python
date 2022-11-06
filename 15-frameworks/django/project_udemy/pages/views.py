from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')  # restrict access when you are not logged in
def page(request, slug: str):

    page = Page.objects.get(slug=slug)

    return render(request, 'pages/page.html', {
        # 'title': page.title,  # it can be done directly from template
        'page': page
    })
