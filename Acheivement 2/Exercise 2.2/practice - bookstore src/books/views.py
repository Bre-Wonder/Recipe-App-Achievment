from django.shortcuts import render
# came with the file
from django.views.generic import ListView, DetailView
# displays a list of books
from .models import Book
# accessing book model
from django.contrib.auth.mixins import LoginRequiredMixin
# meant to project a class based view

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    # specify which model
    model = Book
    # specifies which template
    template_name = 'books/main.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'
