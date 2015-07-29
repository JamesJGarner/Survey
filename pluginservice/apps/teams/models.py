from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):

    name = models.CharField(
        max_length=200
    )

    def __unicode__(self):
        return self.name


class TeamMate(models.Model):

    team = models.ForeignKey(
        Team
    )

    user = models.ForeignKey(
        User
        )

    admin = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = ["team", "user"]


class Invite(models.Model):
    
    invite_from = models.ForeignKey(
        User
        )

    invite_to = models.ForeignKey(
        User,
        related_name='invite_to'
        )

    message = models.TextField(
        null=True,
        blank=True,
        )

    closed = models.BooleanField(
        default=False
        )