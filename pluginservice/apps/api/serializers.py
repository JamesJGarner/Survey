from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from pluginservice.apps.teams.models import Invite
from django.contrib.auth.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']


class InviteSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Invite
        fields = ['message']