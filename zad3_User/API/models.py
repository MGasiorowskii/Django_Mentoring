from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100, null=True)
    published_date = models.IntegerField(null=True)
    categories = models.CharField(max_length=100, null=True)
    thumbnail = models.TextField(null=True)
    book_id = models.CharField(max_length=20, null=True)

