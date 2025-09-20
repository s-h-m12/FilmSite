from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.db.models import Avg, Count

class Genre(models.Model):
    name = models.CharField(unique = True)

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    year = models.IntegerField()
    description = models.TextField(blank = True)
    genres = models.ManyToManyField(Genre)

    def average_rating(self):
        """Расчет среднего рейтинга по конкретному фильму"""
        result = self.review_set.aggregate(Avg('rating'))
        return result['rating__avg']

    def rating_count(self):
        """Количество отзывов на фильм"""
        return self.review_set.count()

class Reviewer(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(blank = True)
    city = models.CharField(max_length = 100, blank = True)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete = models.CASCADE)
    rating = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    text = models.TextField()
    published_at = models.DateTimeField(default = timezone.now)