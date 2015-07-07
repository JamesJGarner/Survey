from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import Homepage, TempProfile
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^profile/$', TempProfile.as_view(), name='TempProfile'),

    url(r'^polls/', include('pluginservice.apps.polls.urls', namespace="polls")),
    url(r'^', include('pluginservice.apps.api.urls', namespace="api")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
