from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.models import User
from .models import Team, TeamMate
from django.core.urlresolvers import reverse


class TeamHome(ListView):
    model = Team

class TeamCreate(CreateView):
    model = Team

    def form_valid(self, form):
        TeamForm = form.save(commit=False)
        self.object = form.save()

        AddUser = TeamMate.objects.create(team=self.object, user=self.request.user, admin=True)
        AddUser.save()

        return super(TeamCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('polls:PollList', kwargs={'pk': self.object.id})