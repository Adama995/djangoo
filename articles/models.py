from django.db import models
from common.models import Base
from django.contrib.auth import get_user_model


class Article(Base):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(
        get_user_model(), related_name="articles_sold", on_delete=models.CASCADE
    )
    price = models.IntegerField()
