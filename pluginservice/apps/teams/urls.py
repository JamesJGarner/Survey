from django.conf.urls import patterns, url
from .views import TeamHome, TeamCreate, InviteResponse, InviteUser

urlpatterns = patterns(
    '',
    url(r'^$', TeamHome.as_view(), name='home'),
    url(r'^create$', TeamCreate.as_view(), name='Create'),
    url(r'^invitereponse/$', InviteResponse.as_view(), name='Create'),
    url(r'^invite/$', InviteUser.as_view(), name='Create'),
    
    
)
