from django.views.generic import TemplateView
from django.contrib.auth.models import User



class TeamHome(TemplateView):
    template_name = 'teams/team_home.html'

    