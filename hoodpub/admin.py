from django.contrib import admin
from .models import Book, UserBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'barcode',
        'author',
        'image_tag',
        'category',
        'ebook_barcode',
        'etc_author',
        'isbn',
        'isbn13',
        'link',
        'list_price',
        'pub_date',
        'pub_nm',
        'sale_price',
        'sale_yn',
        'status_des',
        'translator',
    )
    list_filter = ('created', 'modified')

    readonly_fields = ('image_tag',)


@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'book',
        'user',
        'code',
        'name',
        'gubun',
    )
    search_fields = ('name',)
