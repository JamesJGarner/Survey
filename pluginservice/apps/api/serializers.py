from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from pluginservice.apps.teams.models import Invite, Team
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff']


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class TeamModelSerializer(ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name']



class InviteSerializer(HyperlinkedModelSerializer):
    invite_from = UserModelSerializer()
    team = TeamModelSerializer()
    class Meta:
        model = Invite
        

        fields = ['invite_from', 'team','message']