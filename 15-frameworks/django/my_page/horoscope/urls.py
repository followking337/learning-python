from django.urls import path, converters
from . import views

urlpatterns = [  # custom URLconf
    # view --> function
    # -Static URL-
    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
    # -Dynamic URL-
    # path('<sign>/', views.get_info_about_sign_zodiac),  # route как аргумент
    # -Path Converter-
    # path('', views.index_http),
    path('', views.index_render, name='horoscope-index'),
    path('type/', views.type_index),
    path('type/<str:element>', views.element_index, name='horoscope-type'),
    path('16/', views.get_info_about_16),                                    # поиск роутов идет сверху вниз
    path('<int:sign>', views.get_info_about_zodiac_by_number),               # превращает аргумент из route в int
    # path('<str:sign>', views.get_info_about_zodiac_http, name='horoscope-name-http'),
    # path('<str:sign>', views.get_info_about_zodiac_render_static, name='horoscope-name-render-static'),
    path('<str:sign>', views.get_info_about_zodiac_render_dynamic, name='horoscope-name-render-dynamic'),
]
