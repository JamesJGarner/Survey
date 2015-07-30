from django.conf.urls import patterns, url
from .views import API, Styles, InviteViewSet, UserViewSet


urlpatterns = patterns(
    '',
    url(r'^api/polls/(?P<pk>\d+).js$', API.as_view(), name='Api'),
    url(r'^api/polls/styles.css$', Styles.as_view(), name='Styles'),
    url('^api/users/$', UserViewSet.as_view()),
)
