from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Author, Book, CarouselSlide
from django.core.cache import cache
from .forms import MailingListForm

# Homepage
class HomePageView(TemplateView):
    template_name = "catalogue/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_releases'] = Book.objects.order_by('pub_date')[:3]
        context['slides'] = CarouselSlide.objects.filter(active=True)
        return context

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
