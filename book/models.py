from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


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
