from django.shortcuts import render
from catalog.models import Book, Author, BookInstance
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_availablee = BookInstance.objects.filter(status__exact='Available').count()
    return render(request, 'index.html')