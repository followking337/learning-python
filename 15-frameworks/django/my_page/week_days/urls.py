from django.urls import path
from . import views

urlpatterns = [  # custom URLconf
    # -Static URL-
    # path('monday/', views.monday),
    # path('tuesday/', views.tuesday),
    # -Dynamic URL-
    # path('<int:day>', views.get_day),
    path('<int:day>', views.get_day_redirected),
    path('<str:day>', views.get_day_tasks, name='week_day'),
    path('', views.index)
]
