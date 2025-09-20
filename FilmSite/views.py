from django.shortcuts import render
from .models import Movie, Review
from django.db.models import Q


def index(request):
    movies = Movie.objects.all()
    reviews = Review.objects.all()

    return render(request, 'index.html', {'movies': movies,
                                                              'reviews': reviews})

def movie(request):
    return render(request,'movie.html')

def reviewer(request):
    return render(request,'reviewer.html')