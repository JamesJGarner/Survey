from django.conf.urls import patterns, url
from .views import ListPolls


urlpatterns = patterns(
    '',
    url(r'^$', ListPolls.as_view(), name='ListPolls'),
)
