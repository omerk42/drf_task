from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel
)
from django.contrib.auth.models import User
# Create your models here.


class Post(
        TimeStampedModel,
        TitleSlugDescriptionModel,):
    """
    """
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["id"]

    # created by
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} - {self.title}'
