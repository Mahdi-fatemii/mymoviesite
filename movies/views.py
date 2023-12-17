from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class GenreWesternViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='Western')
    serializer_class = MovieSerializer


class GenreDramaViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='Drama')
    serializer_class = MovieSerializer


class GenreCrimeViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='Crime')
    serializer_class = MovieSerializer


class GenreWarViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='War')
    serializer_class = MovieSerializer


class GenreAdventureViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='Adventure')
    serializer_class = MovieSerializer


class GenreActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='Action')
    serializer_class = MovieSerializer


class GenreComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genres__icontains='Comedy')
    serializer_class = MovieSerializer
