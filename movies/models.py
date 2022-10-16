from django.conf import settings
from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="image/%Y/%m/%d/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    text = models.TextField()
    movie_id = models.ForeignKey("Movie", default=1, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    watch_again = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.text
