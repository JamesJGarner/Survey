from pluginservice.apps.navigation.models import Page
from django.db.models import Sum

from django import template

register = template.Library()

@register.inclusion_tag("site/navigation.html")
def navigation():
    navigation = Page.objects.all().order_by('ordering')
    return {
        "navigation": navigation
    }
