import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from book.models import UserBookModel

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
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


class HoodpubViewSet(ViewSet):

    def create(self, request, *args, **kwargs):
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

        for ele in res.json()['channel']['item']:
            ubm = UserBookModel(ele['author'], ele['title'], **dict(
                author=ele['author'],
                barcode=ele['barcode'],
                category=ele['category'],
                cover_l_url=ele['cover_l_url'],
            ))
            ubm.save()
            print(ele['author'], ele['title'])

        return Response(dict(res=res.json()))

    def delete(self, requests):
        exist = UserBookModel.exists()
        if exist:
            UserBookModel.delete_table()
        UserBookModel.create_table(read_capacity_units=1, write_capacity_units=1)

        return Response(dict(res=exist))
