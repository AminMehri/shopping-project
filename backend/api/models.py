from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime



class User(AbstractUser):
    email = models.EmailField()
    address = models.CharField(max_length=1024)
    shopcard = models.ManyToManyField('Book', related_name='users', blank=True)
    phone_number = models.IntegerField(blank=True, null=True)



class Author(models.Model):
    full_name = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    cover = models.ImageField(upload_to='media/authors', null=False, blank=False)
    image1 = models.ImageField(upload_to='media/authors')
    image2 = models.ImageField(upload_to='media/authors')
    image3 = models.ImageField(upload_to='media/authors')


    def __str__(self):
        return self.full_name



class Quote(models.Model):
    description = models.TextField(max_length=512)
    source = models.CharField(max_length=128)
    author = models.ManyToManyField(Author, related_name='quotes')


    def __str__(self):
        return self.description[:35]



class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(null=False, blank=False, unique=True)
    cover = models.ImageField(upload_to='media/categories', null=False, blank=False)


    def __str__(self):
        return self.title




class Book(models.Model):
    title =  models.CharField(max_length=128)
    category =  models.ManyToManyField(Category, related_name="books")
    author =  models.ManyToManyField(Author, related_name="books")
    slug = models.SlugField(null=False, blank=False, unique=True)
    description =  models.TextField(max_length=512)
    content =  models.TextField()
    about_book =  models.TextField(default=' ')
    cover =  models.ImageField(upload_to='media/books', null=False, blank=False)
    image =  models.ImageField(upload_to='media/books', null=False, blank=False)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.datetime.now())


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
