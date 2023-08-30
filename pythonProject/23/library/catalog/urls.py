from django.urls import path, re_path
from catalog.views import index, AuthorListView, AuthorDetailView, BookListView, BookDetailView, BookInstanceDetailView


urlpatterns = [
    path('', index, name='index'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', AuthorDetailView.as_view(), name='author-detail'),

    path('books/', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),

    re_path(r'^book-instance/(?P<pk>\d+)$', BookInstanceDetailView.as_view(), name='book-instance-detail'),
]
