from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer, BookPickupLocationSerializer, BookRecipientSerializer
from User_Authentication.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookListByAuthorAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author = self.kwargs['author']
        return Book.objects.filter(author__icontains=author)


class BookListByGenreAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Book.objects.filter(genre__icontains=genre)


class BookListByConditionAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        condition = self.kwargs['condition']
        return Book.objects.filter(condition__icontains=condition)


class PickupLocationAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookPickupLocationSerializer
    permission_classes = [IsAuthenticated]


class InterestedUsersAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs['pk']
        return Book.objects.get(pk=book_id).interested_users.all()


class SelectRecipientAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRecipientSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        book_id = self.kwargs['pk']
        user_id = self.kwargs['user_id']
        book = self.get_object()

        # Check if the user is the owner of the book
        if book.owner != request.user:
            return Response({"error": "You are not the owner of this book."}, status=status.HTTP_403_FORBIDDEN)

        # Update the recipient of the book
        book.recipient = user_id
        book.save()

        return Response({"message": "Recipient selected successfully."}, status=status.HTTP_200_OK)
