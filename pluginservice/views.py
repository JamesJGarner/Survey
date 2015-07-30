from django.views.generic import TemplateView
from pluginservice.apps.accounts.models import EmailNotification
from pluginservice.apps.teams.models import Invite, TeamMate

class Homepage(TemplateView):
    template_name = 'site/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
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
