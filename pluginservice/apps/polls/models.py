from django.db import models
from django.contrib.auth.models import User
from pluginservice.apps.teams.models import Team

class Poll(models.Model):

    title = models.CharField(
        max_length=200,
        )

    question = models.CharField(
        max_length=200,
        )

    image = models.CharField(
        max_length=400,
        blank=True,
        null=True,
        )

    created_by = models.ForeignKey(
        User
        )

    team = models.ForeignKey(
        Team,
        null=True,
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
