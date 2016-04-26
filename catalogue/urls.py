from django.conf.urls import url
from .views import BookList, BookDetail

urlpatterns = [

    url(r'^titles/all/$', BookList.as_view(), name='book_list'),
    url(r'^titles/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),

]
