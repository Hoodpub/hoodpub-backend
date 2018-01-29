import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book, User, UserBook
from .serializers import UserSerializer


class HoodpubViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return super(HoodpubViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword', '자전거')

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
            book, created = Book.objects.update_or_create(
                barcode=ele['barcode'], defaults=ele)
            print(ele)
        return Response(res.json())

    def delete(self, requests):
        # exist = UserBookModel.exists()
        # if exist:
        #     UserBookModel.delete_table()
        #     UserBookModel.create_table(read_capacity_units=1, write_capacity_units=1)

        return Response(dict(res='exist'))
