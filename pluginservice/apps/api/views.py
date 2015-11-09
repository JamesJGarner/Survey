from django.views.generic import DetailView, TemplateView
from pluginservice.apps.polls.models import Poll, Vote, PollAnswer
from pluginservice.apps.teams.models import Invite, TeamMate, Team
from pluginservice.apps.notifications.models import Notification
from rest_framework import viewsets
#from django.http import HttpRequest
from .serializers import InviteSerializer, UserSerializer, NotificationSerializer, PollVoteSerializer, TeamModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import generics, filters
from datetime import datetime

def TeamPlayers(teamID):
    tlist = []

    players = TeamMate.objects.filter(team=teamID)
    invites = Invite.objects.filter(team=teamID, closed=False)

    for player in invites:
        tlist.append(player.invite_to.id)

    for player in players:
        tlist.append(player.user.id)

    return tlist


def YourTeams(userID):
    tlist = []

    results = TeamMate.objects.filter(user=userID)

    for result in results:
        tlist.append(Team.objects.get(id=result.team.id))

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


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of the current Notifications you have.
    """
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        result = Notification.objects.filter(user=user, read=False)
        modify = result

        for item in modify:
            item.read = True
            item.save()

        return result


class PollVoteViewSet(viewsets.ModelViewSet):
    """
    Allows someone to vote on a poll
    """

    serializer_class = PollVoteSerializer
    def get_queryset(self):

        """
        step 1 get all the teams the user is in
        step 2 filter by the polls the users is involved in
        step 3 get all the votes ass
        """

        userteammates = TeamMate.objects.filter(user=self.request.user)
        teams = []
        for teammateobject in userteammates:
            teams.append(teammateobject.team)


        #return Vote.objects.filter(team__in=teams)
        return Vote.objects.filter(choice__poll=1)


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of the current Teams you have.
    """
    serializer_class = TeamModelSerializer

    def get_queryset(self):
        user = self.request.user

        return YourTeams(user)
