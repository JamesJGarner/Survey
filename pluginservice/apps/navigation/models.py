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

    show_in_nav = models.BooleanField(
            default=True,
        )

    html_content = models.TextField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.title

