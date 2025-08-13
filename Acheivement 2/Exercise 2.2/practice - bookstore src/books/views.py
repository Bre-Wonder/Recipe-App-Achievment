from django.shortcuts import render
# came with the file
from django.views.generic import ListView
# displays a list of books
from .models import Book
# accessing book model

# Create your views here.


class BookListView(ListView):
    # specify which model
    model = Book
    # specifies which template
    template_name = 'books/main.html'
