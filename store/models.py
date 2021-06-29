from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:genre_items", args=[self.slug])


SCRIPT_CATEGORY = (

    ('M', 'Movie'),
    ('S', 'Short Film'),
    ('D', 'Documentry'),
    ('T', 'Series')
)
MOVIE_CERTIFICATE = (
    ('U', 'U'), ('U/A', 'U/A'), ('A', 'A')
)


class Script(models.Model):
    title = models.CharField('Title ', max_length=50)
    director = models.CharField('Director', max_length=580)
    writer = models.CharField(max_length=2050)
    cast = models.CharField('Casts', max_length=2000)
    genre = models.ManyToManyField("Genre")
    rating = models.FloatField()
    verdict = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='posters')
    pdf = models.FileField(upload_to='pdf')
    recommended = models.BooleanField(default=True)
    category = models.CharField(
        choices=SCRIPT_CATEGORY, default='Movie', max_length=150)
    certificate = models.CharField(
        choices=MOVIE_CERTIFICATE, default='U/A', max_length=50)
    summary = models.TextField()
    slug = models.SlugField()
    year = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    award_winner = models.BooleanField(default=False)

    class Meta:

        verbose_name_plural = 'Scripts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:script_details", args=[self.slug])

class MovieSearch(models.Model):
    name_of_movie=models.CharField(max_length=150)
    def __str__(self):
        return self.name_of_movie
    