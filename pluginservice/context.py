from django.views.generic import ListView
from pluginservice.apps.navigation.models import Page


def navigation(self):
    return Page.objects.all()
