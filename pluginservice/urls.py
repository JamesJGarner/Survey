from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Homepage, TempProfile, Widgets
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^profile/$', TempProfile.as_view(), name='TempProfile'),
    url(r'^widgets/$', Widgets.as_view(), name='Widgets'),

    url(r'^widgets/polls/', include('pluginservice.apps.polls.urls', namespace="polls")),
    url(r'^', include('pluginservice.apps.api.urls', namespace="api")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
