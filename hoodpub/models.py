from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.safestring import mark_safe
from model_utils.models import TimeStampedModel
from versatileimagefield.fields import VersatileImageField
import wikipedia
wikipedia.set_lang("ko")


class HoodpubUserManager(UserManager):
    def new_from_wiki(self, keyword):
        page = wikipedia.page(keyword)
        username = "%s-%s-%s" % (page.title, page.pageid, "wiki")
        import ipdb; ipdb.set_trace()
        image = page.images[0] if len(page.images) > 0 else None
        self.create_user(username,
                         password=page.title,
                         **dict(last_name=page.title,
                                first_name=page.original_title,
                                image_profile=image))
        return page.title


class User(AbstractUser, TimeStampedModel):
    image_profile = VersatileImageField(
        'Image',
        upload_to='images/user/',
        blank=True,
        null=True
    )
    url_wiki = models.URLField(max_length=512, null=True, blank=True)
    objects = HoodpubUserManager()

    class Meta:
        unique_together = (("username", "url_wiki"),)

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, *kwargs)


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
    user = models.ForeignKey(User, related_name='userbooks', on_delete=models.CASCADE)
    url_refer = models.URLField(max_length=512, null=True, blank=True)
    verified = models.BooleanField(default=False)
