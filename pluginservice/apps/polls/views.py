from django.views.generic import ListView, CreateView, TemplateView, DetailView
from .models import Poll
from django.core.urlresolvers import reverse



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

