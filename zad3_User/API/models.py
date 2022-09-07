from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    published_data = models.IntegerField()
    categories = models.CharField(max_length=100)
    thumbnail = models.TextField()

