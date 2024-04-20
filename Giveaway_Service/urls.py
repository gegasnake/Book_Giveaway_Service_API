from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    path('books/<uuid:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book_detail'),
]
