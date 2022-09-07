from django.urls import path
from .views import GetAllBooks, UpdateDataBase

urlpatterns = [
    path('books/', GetAllBooks.as_view(), name='get_books'),
    path('db/', UpdateDataBase.as_view(), name='update_db'),
]
