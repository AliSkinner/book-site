from django.conf.urls import url
from .views import BookList, BookDetail, AuthorList, AuthorDetail, HomePageView

urlpatterns = [

    # landing page
    url(r'^$', HomePageView.as_view(), name='homepage'),

    # titles
    url(r'^titles/$', BookList.as_view(), name='book_list'),
    url(r'^titles/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),

    # authors
    url(r'^authors/$', AuthorList.as_view(), name='author_list'),
    url(r'^authors/(?P<slug>[-\w]+)/$', AuthorDetail.as_view(), name='author_detail'),


]
