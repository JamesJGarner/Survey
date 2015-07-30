from django.views.generic import DetailView, TemplateView
from pluginservice.apps.polls.models import Poll
from pluginservice.apps.teams.models import Invite
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
    queryset = User.objects.all()
    serializer = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')



class InviteViewSet(viewsets.ReadOnlyModelViewSet):
    model = Invite
    """
    Returns a list of the current invites you have
    """

    print Invite.invite_from


    queryset = Invite.objects.filter(
        invite_to=1,
        closed=False,
    )
    serializer_class = InviteSerializer

