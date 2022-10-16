from django.urls import path

from .views import (
    MovieCreateView,
    MovieDeleteView,
    MovieDetailView,
    MovieListView,
    MovieUpdateView,
    ReviewCreateView,
    SearchResultsListView,
)

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("movies/new/", MovieCreateView.as_view(), name="movie_new"),
    path("movies/<int:pk>/edit/", MovieUpdateView.as_view(), name="movie_edit"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie_delete"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("review/new/", ReviewCreateView.as_view(), name="review_new"),
]
