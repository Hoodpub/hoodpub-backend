from django.utils.html import mark_safe
from django.contrib import admin
from .models import User, Book, UserBook


class UserBookInline(admin.TabularInline):
    model = UserBook

    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'id',
        'first_name',
        'last_name',
        'email',
        'image_profile_tag',
        'date_joined',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'created',
        'modified',
    )
    raw_id_fields = ('groups', 'user_permissions')
    inlines = (UserBookInline, )

    def image_profile_tag(self, obj):
        if not obj.image_profile:
            return None

        return mark_safe('<img src="{}" />'.format(obj.image_profile.thumbnail['100x100'].url))

    image_profile_tag.short_description = 'Image'


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
        'url_refer',
        'verified',
    )
    list_filter = ('created', 'modified', 'book', 'user', 'verified')
