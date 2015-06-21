from django.views.generic import DetailView
from pluginservice.apps.polls.models import Poll
#from django.http import HttpRequest


# Not important right now
class API(DetailView):
    model = Poll
