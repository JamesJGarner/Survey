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


class Styles(TemplateView):
    template_name = 'site/styles.html'


class UserViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        team = self.kwargs['team']
        queryset = User.objects.filter()

        if team:
            teams = TeamMate.objects.filter(team=team)
            exclude = []
            for person in teams:
                exclude.append(person.user.id)
            queryset = User.objects.exclude(pk__in=exclude)

        serializer = UserSerializer
        filter_backends = (filters.SearchFilter,)
        search_fields = ('username', 'email')
        return queryset



class InviteViewSet(generics.ListAPIView):
    serializer_class = InviteSerializer

    def get_queryset(self):
        """
        Returns a list of the current invites you have
        """
        user = self.request.user
        print user
        return Invite.objects.filter(invite_to=user, closed=False)