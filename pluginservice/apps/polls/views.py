from django.views.generic import ListView, CreateView
from .models import Poll


# Not important right now
class PollList(ListView):
    model = Poll

class PollCreate(CreateView):
	model = Poll
