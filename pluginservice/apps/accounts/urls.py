from django.conf.urls import patterns, url
from .views import CreateAccount, ChangePassword

urlpatterns = patterns(
    '',
    url(r'^register/$', CreateAccount.as_view(), name='Create'),
    url(r'^profile/password/$', ChangePassword, name='Changepwd'),
)
