from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from .views import Homepage, TempProfile, Widgets, PollJS
from pluginservice.apps.navigation.views import PageDetail
from apps.api.views import InviteViewSet, UserViewSet, NotificationViewSet, PollVoteViewSet, TeamViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'invites', InviteViewSet, base_name='invites')
router.register(r'notifications', NotificationViewSet, base_name='notifications')
router.register(r'votes', PollVoteViewSet, base_name='votes')
router.register(r'teams', TeamViewSet, base_name='teams')

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^profile/$', TempProfile.as_view(), name='TempProfile'),
    #url(r'^widgets/$', Widgets.as_view(), name='Widgets'),
    url(r'^widgets/polls/', include('pluginservice.apps.polls.urls', namespace="polls")),
    url(r'^team/', include('pluginservice.apps.teams.urls', namespace="teams")),
    url(r'^', include('pluginservice.apps.accounts.urls', namespace="accounts")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^api/', include(router.urls)),
    url(r'^api/widgets/polls/(?P<pk>\d+).js$', PollJS.as_view(), name='PollList'),
    url(r"^(?P<page_slug>[^/]+)/$", PageDetail.as_view(), name="page_slugs"),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
