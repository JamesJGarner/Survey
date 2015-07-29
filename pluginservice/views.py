from django.views.generic import TemplateView
from pluginservice.apps.accounts.models import EmailNotification

class Homepage(TemplateView):
    template_name = 'site/homepage.html'


class TempProfile(TemplateView):
    template_name = 'site/profile.html'

    def get_context_data(self, **kwargs):
        context = super(TempProfile, self).get_context_data(**kwargs)
        context['EmailNotification'] = EmailNotification.objects.all()
        return context    


class Widgets(TemplateView):
    template_name = 'site/widgets.html'
