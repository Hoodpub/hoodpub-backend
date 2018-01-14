import json

import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        keyword = kwargs.get('keyword', '자연')

        url = 'https://apis.daum.net/search/book?apikey=9f68e425f40e190b407745eb855619262ce0b2cc&q=%s&output=json' % keyword
        res = requests.get(url)
        return Response(dict(res=res.json()))
