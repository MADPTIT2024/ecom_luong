from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, AuthorListCreate, AuthorRetrieveUpdateDestroy, PublisherListCreate, PublisherRetrieveUpdateDestroy, BookListCreate, BookRetrieveUpdateDestroy,ProductSearchAPIView

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),

    path('authors/', AuthorListCreate.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-detail'),

    path('publishers/', PublisherListCreate.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherRetrieveUpdateDestroy.as_view(), name='publisher-detail'),

    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail'),
    path('books/search/', ProductSearchAPIView.as_view(), name='product-search'),
]
