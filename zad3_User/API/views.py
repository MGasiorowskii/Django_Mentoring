from rest_framework.viewsets import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class GetAllBooks(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class UpdateDataBase(APIView):

    def post(self, request):
        url = 'https://www.googleapis.com/books/v1/volumes'
        params = request.data

        res = requests.get(url=url, params=params)
        data = res.json()

        print(data)

        return Response(status=status.HTTP_201_CREATED)
