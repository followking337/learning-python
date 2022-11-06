"""my_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from horoscope.views import leo, scorpio
# from horoscope import views
from horoscope import views as views_horoscope
from week_days import views as views_week_days

urlpatterns = [  # URLconf
    path('admin/', admin.site.urls),
    # path('horoscope/leo/', views_horoscope.leo),
    # path('horoscope/scorpio/', views_horoscope.scorpio),
    path('horoscope/', include('horoscope.urls')),  # without .py, connect no custom URLconf
    # path('todo_week/monday/', views_week_days.monday),
    # path('todo_week/tuesday/', views_week_days.tuesday),
    path('todo_week/', include('week_days.urls')),  # without .py
    path('calculate_geometry/', include('geometry.urls')),
]
