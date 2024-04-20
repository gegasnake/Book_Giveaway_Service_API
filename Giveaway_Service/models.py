import uuid
from django.db import models
from User_Authentication.models import CustomUser


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


class Genre(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, default=uuid.uuid4, on_delete=models.CASCADE)
    interested_users = models.ManyToManyField(CustomUser, related_name='interested_books', through='OwnershipDecision')
    pickup_location = models.CharField(max_length=255)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OwnershipDecision(models.Model):
    user = models.ForeignKey(CustomUser, default=uuid.uuid4, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, default=uuid.uuid4, on_delete=models.CASCADE)
    chosen_recipient = models.BooleanField(default=False)

    def __str__(self):
        return f"OwnershipDecision: {self.user.username} - {self.book.title}"