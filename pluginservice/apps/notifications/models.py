from django.contrib.auth.models import User
from django.db import models



class Notification(models.Model):

    user = models.ForeignKey(
        User
    )

    title = models.CharField(
    	max_length=200,
    	)

    text = models.TextField()

    read = models.BooleanField(
    	default=False
    	)

    def __unicode__(self):
        return self.title


