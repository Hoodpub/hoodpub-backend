from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Book, User, UserBook


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
    image_profile = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = User
        exclude = ['created', 'modified', 'password', 'last_login',
                   'is_superuser', 'last_name', 'is_staff',
                   'date_joined', 'groups', 'user_permissions']
