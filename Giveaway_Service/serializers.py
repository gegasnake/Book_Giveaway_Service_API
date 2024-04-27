# serializers.py

from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['interested_users']


class BookPickupLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pickup_location']




