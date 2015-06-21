from django.views.generic import ListView
from .models import Poll


# Not important right now
class ListPolls(ListView):
    model = Poll


