from rest_framework.viewsets import generics
from .serializers import ArticleSerializers
from first_project.blog.models import Article


class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
