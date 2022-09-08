from django.urls import path
from .views import GetAllBooks, UpdateDataBase, DetailBook

urlpatterns = [
    path('books/', GetAllBooks.as_view(), name='get_books'),
    path('db/', UpdateDataBase.as_view(), name='update_db'),
    path('books/<bookId>', DetailBook.as_view(), name='get_bookId'),
]
