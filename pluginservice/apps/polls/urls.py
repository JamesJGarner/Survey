from django.conf.urls import patterns, url
from .views import PollList, PollCreate, PollCreateSuccess, PollDetail, PollHome


urlpatterns = patterns(
    '',
    url(r'^$', PollHome.as_view(), name='PollHome'),
    url(r'^manage/$', PollList.as_view(), name='PollList'),
    url(r'^create/$', PollCreate.as_view(), name='PollCreate'),
    url(r'^manage/(?P<pk>\d+)/$', PollDetail.as_view(), name='PollDetail'),
    url(r'^manage/(?P<pk>\d+)/help/$', PollCreateSuccess.as_view(), name='success'),
)
