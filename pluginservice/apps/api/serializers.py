from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from pluginservice.apps.teams.models import Invite

class InviteSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Invite
        fields = ['message']