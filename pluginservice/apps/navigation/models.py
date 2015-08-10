from django.contrib.auth.models import User
from django.db import models


class Page(models.Model):

    title = models.CharField(
        max_length=200,
    )

    slug = models.CharField(
        max_length=200,
        unique=True,
    )

    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
    )

    ordering = models.IntegerField(
        null=True,
        )

    def __unicode__(self):
        return self.title

