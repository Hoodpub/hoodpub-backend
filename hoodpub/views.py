import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book, UserBook


class HoodpubViewSet(ModelViewSet):
    queryset = UserBook.objects.all()

    def list(self, request, *args, **kwargs):
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

    def create(self, request, *args, **kwargs):
        # for ele in res.json()['channel']['item']:
        #     ubm = UserBookModel(ele['author'], ele['title'], **dict(
        #         author=ele['author'],
        #         barcode=ele['barcode'],
        #         category=ele['category'],
        #         cover_l_url=ele['cover_l_url'],
        #     ))
        #     ubm.save()
        #     # print(ele['author'], ele['title'])
        # print("DB name %s", os.getenv('RDB_NAME'))

        return Response(dict(res='hi'))

    def delete(self, requests):
        # exist = UserBookModel.exists()
        # if exist:
        #     UserBookModel.delete_table()
        #     UserBookModel.create_table(read_capacity_units=1, write_capacity_units=1)

        return Response(dict(res='exist'))
