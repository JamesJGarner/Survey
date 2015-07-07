from django.views.generic import ListView, CreateView, TemplateView, DetailView
from .models import Poll
from django.core.urlresolvers import reverse
from pluginservice.settings.production import CURRENT_SITE_URL


# Not important right now
class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

class PollCreate(CreateView):
    model = Poll
    #success_url = '/polls/create/success/'
    
    def get_success_url(self, **kwargs):         
        return reverse('polls:success', kwargs={'pk': self.object.id})

class PollCreateSuccess(DetailView):
    model = Poll
    template_name = 'polls/poll_success.html'

    def get_context_data(self, **kwargs):
        context = super(PollCreateSuccess, self).get_context_data(**kwargs)
        context['current_site_url'] = CURRENT_SITE_URL
        return context