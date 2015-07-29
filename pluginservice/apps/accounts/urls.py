from django.conf.urls import patterns, url
from .views import CreateAccount

urlpatterns = patterns(
    '',
    url(r'^register/$', CreateAccount.as_view(), name='Create'),
)
