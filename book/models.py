from django.db import models
from model_utils.models import TimeStampedModel

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Book(TimeStampedModel):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32, unique=True)
    gubun = models.CharField(max_length=32)


class UserBookModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "user-book"
        region = 'ap-northeast-2'

    user = UnicodeAttribute(range_key=True)
    book = UnicodeAttribute(hash_key=True)
    author = UnicodeAttribute(null=True)
    barcode = UnicodeAttribute(null=True)
    category = UnicodeAttribute(null=True)
    cover_l_url = UnicodeAttribute(null=True)
