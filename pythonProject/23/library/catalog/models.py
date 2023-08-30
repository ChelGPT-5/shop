from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pseudonym = models.CharField(max_length=250)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.pseudonym

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.pk)])


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])


class BookInstance(models.Model):
    STATUSES = (
        ('Available', 'Available'),
        ('On Loan', 'On Loan'),
        ('Lost', 'Lost')
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateTimeField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUSES, default='Available')
