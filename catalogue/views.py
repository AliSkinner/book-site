from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book

# show all books
class BookList(ListView):
    model = Book
    paginate_by = 12

# show individual book
class BookDetail(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        # Get books by same author
        context['related_books'] = Book.objects.filter(author=self.object.author).exclude(id=self.object.id)
        return context

# show all author
class AuthorList(ListView):
    model = Author
    paginate_by = 12

# show individual author
class AuthorDetail(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        # Get books by same author
        context['related_books'] = Book.objects.filter(author=self.object)
        return context
