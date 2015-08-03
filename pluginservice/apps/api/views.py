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


def TeamPlayers(teamID):
    tlist = []
    players = TeamMate.objects.filter(team=teamID)
    
    for player in players:
        tlist.append(player.user.id)

    return tlist


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View the detail of a user and filter by team the avalible users that can be invited
    """
    def get_queryset(self):
        inviteable = self.request.query_params.get('inviteable', None)
        team = self.request.query_params.get('team', None)
        queryset = User.objects.all();

        if inviteable:
            tlist = TeamPlayers(inviteable)
            return User.objects.exclude(pk__in=tlist)

        if team:
            tlist = TeamPlayers(team)
            return User.objects.filter(pk__in=tlist)

        
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

