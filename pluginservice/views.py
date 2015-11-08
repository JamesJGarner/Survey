from django.views.generic import TemplateView, DetailView
from pluginservice.apps.accounts.models import EmailNotification
from pluginservice.apps.teams.models import Invite, TeamMate
from pluginservice.apps.polls.models import Poll


class Homepage(TemplateView):
    template_name = 'site/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            Listofteams = []

            TeamMateList = TeamMate.objects.filter(user=self.request.user)

            for mate in TeamMateList:
                Listofteams.append(mate.team)

            context ['polls'] = Poll.objects.filter(team__in=Listofteams)

            context['teams'] = TeamMate.objects.filter(user=self.request.user)

            context['invites'] = Invite.objects.filter(invite_to=self.request.user, closed=False)
        return context


class TempProfile(TemplateView):
    template_name = 'site/profile.html'

    def get_context_data(self, **kwargs):
        context = super(TempProfile, self).get_context_data(**kwargs)
        context['EmailNotification'] = EmailNotification.objects.all()
        return context


class Widgets(TemplateView):
    template_name = 'site/widgets.html'


# Not important right now
class PollJS(DetailView):
    model = Poll
    template_name = 'site/js.html'
