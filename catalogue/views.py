from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

    # def get_context_data(self, **kwargs):
    #     context = super(BookDetail, self).get_context_data(**kwargs)
    #     # context['now'] = timezone.now()
    #     return context
