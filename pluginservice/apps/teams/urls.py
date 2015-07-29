from django.conf.urls import patterns, url
from .views import TeamHome, TeamCreate

urlpatterns = patterns(
    '',
    url(r'^$', TeamHome.as_view(), name='home'),
    url(r'^create$', TeamCreate.as_view(), name='Create'),

    
)
