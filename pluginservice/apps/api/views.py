from django.views.generic import DetailView, TemplateView
from pluginservice.apps.polls.models import Poll
#from django.http import HttpRequest


# Not important right now
class API(DetailView):
    model = Poll
    template_name = 'site/js.html'


class Styles(TemplateView):
    template_name = 'site/styles.html'
