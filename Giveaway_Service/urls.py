from django.urls import path
from .views import (BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, BookListByAuthorAPIView,
                    BookListByGenreAPIView, BookListByConditionAPIView,
                    PickupLocationAPIView, InterestedUsersAPIView, SelectRecipientAPIView)


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create'),
    path('books/<uuid:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book_detail'),
    path('books/filter/author/<str:author>/', BookListByAuthorAPIView.as_view(), name='book_list_by_author'),
    path('books/filter/genre/<str:genre>/', BookListByGenreAPIView.as_view(), name='book_list_by_genre'),
    path('books/filter/condition/<str:condition>/', BookListByConditionAPIView.as_view(),
         name='book_list_by_condition'),
    path('books/<uuid:pk>/pickup-location/', PickupLocationAPIView.as_view(), name='pickup_location'),
    path('books/<uuid:pk>/owners/', InterestedUsersAPIView.as_view(), name='interested_users'),
    path('books/<uuid:pk>/owners/<int:user_id>/', SelectRecipientAPIView.as_view(), name='select_recipient'),
]
