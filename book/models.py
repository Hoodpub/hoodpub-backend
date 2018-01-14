from django.db import models
from model_utils.models import TimeStampedModel


class Book(TimeStampedModel):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=32, unique=True)
    gubun = models.CharField(max_length=32)
