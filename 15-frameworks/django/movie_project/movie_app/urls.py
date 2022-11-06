from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/keanu', views.keanu),
    path('worldrecords', views.get_guinness_world_records),
    # path('movie/<int:id_movie>', views.show_one_movie, name='movie-detail'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('director/', views.show_all_directors, name='directors-list'),
    path('director/<int:index>', views.director_ditail, name='director-detail'),
    path('actor/', views.show_all_actors, name='actors-list'),
    path('actor/<int:index>', views.actor_ditail, name='actor-detail'),
]
