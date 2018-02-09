import requests
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book, User
from .serializers import UserSerializer


class HoodpubViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super(HoodpubViewSet, self).get_queryset()
        queryset = queryset.annotate(count=Count('userbooks')).order_by('-count')

        return queryset

    def list(self, request, *args, **kwargs):
        return super(HoodpubViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        keyword = request.data.get('keyword', '자전거')

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
