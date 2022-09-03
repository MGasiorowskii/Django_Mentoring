from django.shortcuts import render
from .models import Article


def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class HomeViewSet():
    def get(self):
        pass

    def list(self):
        pass

    def update(self):
        pass
