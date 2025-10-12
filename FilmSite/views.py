from django.shortcuts import render, get_object_or_404
from .models import Movie, Review, Reviewer
from django.db.models import Q


def index(request):
    movies = Movie.objects.all()
    reviews = Review.objects.all()

    return render(request, 'index.html', {'movies': movies,
                                                              'reviews': reviews})

def movie_detail(request, id):
    movie = get_object_or_404(Movie.objects.prefetch_related('genres', 'review_set__reviewer'), id = id)
    return render(request,'movie.html', {'movie': movie})

def reviewer_detail(request, id):
    reviewer = get_object_or_404(Reviewer, id=id)
    reviews = Review.objects.filter(reviewer=reviewer).select_related('movie').order_by('-published_at')
    return render(request, 'reviewer.html', {'reviewer': reviewer, 'reviews': reviews})