from django.conf.urls import patterns, url
from .views import API, Styles, InviteViewSet, UserViewSet, UserDetailViewSet


urlpatterns = patterns(
    '',
    url(r'^api/polls/(?P<pk>\d+).js$', API.as_view(), name='Api'),
    url(r'^api/polls/styles.css$', Styles.as_view(), name='Styles'),
    url('^api/users/(?P<team>.+)/$', UserViewSet.as_view()),
    url('^api/invites/$', InviteViewSet.as_view()),
    url('^api/user/(?P<pk>.+)/$', UserDetailViewSet.as_view()),
)
