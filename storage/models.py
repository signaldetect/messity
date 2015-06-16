"""
Models of the `storage` app
"""

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
