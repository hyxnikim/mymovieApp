from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Movie
from .models import Review
# Create your views here.
#index == movie_list
#generic == movie_detail

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def index(request):
    movies = Movie.objects.all()
    reviews = Review.objects.all()
    context = {
        'movie' : movies,
    }
    return render(request,'review_data/index.html', context)

def generic(request, no):
    movie = Movie.objects.get(no=no)
    reviews = Review.objects.filter(movie=no)

    context = {
        'movie' : movie,
        'review' : reviews,
    }
    return render(request, 'review_data/generic.html', context)

"""
def elements(request):
    return render(request,'review_data/elements.html', {})
def generic(request):
    return render(request,'review_data/generic.html', {})
"""
