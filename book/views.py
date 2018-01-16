import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        print('version')
        keyword = request.GET.get('keyword', '자연')

        payload = {
            "output": "json",
            "result": 20,
            "apikey": "9f68e425f40e190b407745eb855619262ce0b2cc",
            "searchType": "title"
        }

        if keyword:
            payload['q'] = keyword

        url = 'https://apis.daum.net/search/book'
        res = requests.get(url, params=payload)
        return Response(dict(res=res.json()))
