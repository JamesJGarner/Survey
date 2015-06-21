from django.conf.urls import patterns, url
from .views import API

urlpatterns = patterns(
    '',
    url(r'^api/polls/(?P<pk>\d+)$', API.as_view(), name='Api'),
)
