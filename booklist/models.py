from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=20)


class Location(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField('Category', related_name='books')

    location= models.OneToOneField('Location', related_name='books',on_delete=models.CASCADE)


class Comment(models.Model):

    author = models.CharField(max_length=60)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey('Book', on_delete=models.CASCADE)


