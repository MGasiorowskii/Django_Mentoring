from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializers
from blog.models import Article


class GetAllArticles(generics.ListAPIView):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


class GetArticle(generics.RetrieveAPIView):
    serializer_class = ArticleSerializers
    queryset = Article


class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializers
    permission_classes = [IsAuthenticated]
