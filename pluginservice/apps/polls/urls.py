from django.conf.urls import patterns, url
from .views import PollList, PollCreate


urlpatterns = patterns(
    '',
    url(r'^manage/$', PollList.as_view(), name='PollList'),
    url(r'^create/$', PollCreate.as_view(), name='PollCreate'),
)
