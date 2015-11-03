from django.conf.urls import patterns, url
from .views import PollCreate, PollCreateSuccess, PollDetail, PollHome


urlpatterns = patterns(
    '',
    #url(r'^$', PollHome.as_view(), name='PollHome'),
    url(r'^create/$', PollCreate.as_view(), name='PollCreate'),
    url(r'^(?P<pk>\d+)/$', PollDetail.as_view(), name='PollDetail'),
    url(r'^(?P<pk>\d+)/help/$', PollCreateSuccess.as_view(), name='success'),
)
