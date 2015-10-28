from django.conf.urls import patterns, url
from .views import CreateAccount, ChangePassword, TutorialForm

urlpatterns = patterns(
    '',
    url(r'^register/$', CreateAccount.as_view(), name='Create'),
    url(r'^profile/password/$', ChangePassword, name='Changepwd'),
    url(r'^tutorial/completed/', TutorialForm.as_view(), name='complete'),
)
