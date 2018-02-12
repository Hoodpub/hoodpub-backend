from django.db.models import Count
from rest_framework import filters
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from daumapi.search import Search

from .models import Book, User
from .serializers import UserSerializer


class UserBookViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('username',)
    filter_fields = ('first_name',)

    def get_queryset(self):
        queryset = User.objects.annotate(count=Count('userbooks')).order_by('-count')

        return queryset

    def list(self, request, *args, **kwargs):
        response = super(UserBookViewSet, self).list(request, *args, **kwargs)

        if len(response.data):
            return response

        search = request.GET.get('search', None)
        User.objects.new_from_wiki(keyword=search)
        return super(UserBookViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        keyword = request.data.get('keyword', '자전거')
        res = self._add_books(keyword)
        return Response(res)

    def _add_books(self, keyword):
        search = Search()
        res = search.request(keyword=keyword)

        for ele in res['items']:
            book, created = Book.objects.update_or_create(barcode=ele['barcode'], defaults=ele)

        return res

    @list_route(methods=['post'])
    def add_user(self, request, *args, **kwargs):
        keyword = request.data.get('keyword', '자전거')
        user = User.objects.new_from_wiki(keyword)
        return Response(dict(message=user), status=status.HTTP_201_CREATED)
