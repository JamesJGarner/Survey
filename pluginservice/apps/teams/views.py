from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.contrib.auth.models import User
from .models import Team, Invite, TeamMate
from django.core.urlresolvers import reverse
from .forms import InviteResponseForm, InviteUserForm

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


class InviteUser(CreateView):
    model = Invite
    form_class = InviteUserForm
    success_url = '/'

    def form_valid(self, form):
        TeamForm = form.save(commit=False)
        TeamForm.invite_from = self.request.user
        self.object = form.save()
        return super(InviteUser, self).form_valid(form)

class InviteResponse(FormView):
    template_name = 'teams/teammate_form.html'
    form_class = InviteResponseForm
    success_url = '/'
    def form_valid(self, form):
        # do the thing
        inviteid = form.cleaned_data["invite_id"]

        inviteobject = Invite.objects.get(id=inviteid)

        # Is this user in the group as well?
        
        if inviteobject.invite_to == self.request.user:
            inviteobject.closed = True
            inviteobject.save()
            try:
                TeamMate.objects.create(team=inviteobject.team, user=inviteobject.invite_to, admin=False)
            except:
                print "failed"

        print form.cleaned_data["accept"]
        return super(InviteResponse, self).form_valid(form)

