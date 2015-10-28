from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class EmailNotification(models.Model):

    title = models.CharField(
        max_length=200
    )

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        )

    balance = models.DecimalField(
        max_digits=100,
        default=0.00,
        decimal_places=2,
    )

    email_notifications = models.ManyToManyField(
        EmailNotification,
        null=True,
        blank=True,
        )

    profile_picture = models.ImageField(
        default='../static/img/default.png',
        upload_to='%Y/%m/%d'
        )

    tutorial_completed = models.BooleanField(
        default=False,  
        )

    def __unicode__(self):
        return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        up = UserProfile(user=user)
        up.save()

post_save.connect(create_profile, sender=User)
