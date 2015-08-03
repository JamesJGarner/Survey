from django.views.generic import DetailView, TemplateView
from pluginservice.apps.polls.models import Poll
from pluginservice.apps.teams.models import Invite, TeamMate
from rest_framework import viewsets
#from django.http import HttpRequest
from .serializers import InviteSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import generics, filters


# Not important right now
class API(DetailView):
    model = Poll
    template_name = 'site/js.html'


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View the detail of a user and filter by team the avalible users that can be invited
    """
    def get_queryset(self):
        team = self.request.query_params.get('team', None)
        print team
        exclude = []

        if team:
            teams = TeamMate.objects.filter(team=team)
            for person in teams:
                exclude.append(person.user.id)
        
        queryset = User.objects.exclude(pk__in=exclude)
        return queryset

    serializer_class = UserSerializer
    serializer = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')


class InviteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of the current invites you have.
    """
    serializer_class = InviteSerializer

    def get_queryset(self):

        user = self.request.user
        print user
        return Invite.objects.filter(invite_to=user, closed=False)

