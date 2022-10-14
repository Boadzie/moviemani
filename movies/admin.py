from django.contrib import admin

from .models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    search_fields = ["title"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["text", "watch_again"]
    search_fields = ["text"]
