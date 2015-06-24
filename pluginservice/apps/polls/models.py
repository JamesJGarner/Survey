from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):

    title = models.CharField(
        max_length=200,
        )

    question = models.CharField(
        max_length=200,
        )

    created_by = models.ForeignKey(
        User
        )

    deleted = models.BooleanField(
        default=False,
        )

    def __unicode__(self):
        return self.title


class PollAnswer(models.Model):

    poll = models.ForeignKey(
        Poll,
        )

    answer = models.CharField(
        max_length=200,
        )
