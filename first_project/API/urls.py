from django.urls import path
from .views import GetAllArticles


urlpatterns = [
    path('articles/', GetAllArticles.as_view(), name='get_articles')
]
