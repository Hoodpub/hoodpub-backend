from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from model_utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    pass


class Book(TimeStampedModel):
    barcode = models.CharField(max_length=32, unique=True)
    author = models.CharField(max_length=32)
    category = models.CharField(max_length=32, null=True, blank=True)
    cover_l_url = models.URLField(max_length=512, null=True, blank=True)
    cover_s_url = models.URLField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ebook_barcode = models.CharField(max_length=32, null=True, blank=True)
    etc_author = models.CharField(max_length=32, null=True, blank=True)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    isbn13 = models.CharField(max_length=32, null=True, blank=True)
    link = models.CharField(max_length=512, null=True, blank=True)
    list_price = models.IntegerField(default=0)
    pub_date = models.CharField(max_length=32, null=True, blank=True)
    pub_nm = models.CharField(max_length=32, null=True, blank=True)
    sale_price = models.IntegerField(default=0)
    sale_yn = models.CharField(max_length=32, null=True, blank=True)
    status_des = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    translator = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return '%s  %s' % (self.title, self.sale_price)

    def image_tag(self):

        return mark_safe('<img src="%s" />' % self.cover_l_url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class UserBook(TimeStampedModel):
    book = models.ForeignKey(Book, related_name='userbooks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='userbooks2', on_delete=models.CASCADE)
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32, unique=True)
    gubun = models.CharField(max_length=32)
