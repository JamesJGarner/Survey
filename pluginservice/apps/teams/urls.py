from django.conf.urls import patterns, url
from .views import TeamList, TeamDetail,TeamCreate, InviteResponse, InviteUser

urlpatterns = patterns(
    '',
    url(r'^$', TeamList.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', TeamDetail.as_view(), name='TeamDetail'),
    url(r'^create/$', TeamCreate.as_view(), name='Create'),
    url(r'^invitereponse/$', InviteResponse.as_view(), name='Create'),
    url(r'^invite/$', InviteUser.as_view(), name='Create'),
    
    
    
)
