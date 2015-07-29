from django.conf.urls import patterns, url
from .views import TeamHome

urlpatterns = patterns(
    '',
    url(r'^$', TeamHome.as_view(), name='Create'),
)
