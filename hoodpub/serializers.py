from rest_framework import serializers
from .models import Book, UserBook, User


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ['created', 'modified']


class UserBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBook
        exclude = ['created', 'modified']


class UserSerializer(serializers.ModelSerializer):
    userbooks = UserBookSerializer(many=True)

    class Meta:
        model = User
        exclude = ['created', 'modified']
