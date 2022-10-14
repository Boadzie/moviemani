from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Movie


class MovieListView(ListView):
    model = Movie
    context_object_name = "movies"
    template_name = "movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"


class MovieCreateView(CreateView):
    model = Movie
    fields = ["title", "description", "image"]
    template_name = "movie_new.html"


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["title", "description", "image"]
    template_name = "movie_edit.html"


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    success_url = reverse_lazy("movie_list")


class SearchResultsListView(ListView):  # new
    model = Movie
    context_object_name = "movie_list"
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        return Movie.objects.filter(Q(title__icontains=query.lower()))
