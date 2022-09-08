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
        if request.data:
            url = 'https://www.googleapis.com/books/v1/volumes'
            params = request.data

            res = requests.get(url=url, params=params)
            data = res.json()
            Book.objects.all().delete()

            for item in data["items"]:

                book = item["volumeInfo"]

                book_id = item['id']
                title = book.setdefault("title")
                authors = book.setdefault("authors")
                published_date = book.setdefault("publishedDate")
                categories = book.setdefault("categories")
                thumbnail = book["imageLinks"]["thumbnail"]

                Book.objects.create(book_id=book_id,
                                    title=title,
                                    authors=authors,
                                    published_date=published_date,
                                    categories=categories,
                                    thumbnail=thumbnail)

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class DetailBook(APIView):

    def get(self, request, bookId):
        queryset = Book.objects.all().get(book_id=bookId)
        serializer = BookSerializer(queryset)

        return Response(serializer.data)


