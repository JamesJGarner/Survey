from django.views.generic import TemplateView, CreateView, ListView, FormView, DetailView
from django.contrib.auth.models import User
from .models import Team, Invite, TeamMate
from django.core.urlresolvers import reverse
from .forms import InviteResponseForm, InviteUserForm
from pluginservice.apps.polls.views import owner, isUserAdmin
from pluginservice.apps.polls.models import Poll

class TeamList(ListView):
    model = Team

    def get_queryset(self):
        teamlist = []

        for team in Team.objects.all():
            if owner(self, team.id):
                teamlist.append(team.id)

        queryset = Team.objects.filter(id__in=teamlist)
        return queryset



class TeamDetail(DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data(**kwargs)
        context['poll_list'] = Poll.objects.filter(team=self.kwargs['pk'])  
        context['admin'] = isUserAdmin(self)
        teamid = self.kwargs['pk']
        if not owner(self, teamid):
            raise Http404

        return context



class TeamCreate(CreateView):
    model = Team

    def form_valid(self, form):
        TeamForm = form.save(commit=False)
        self.object = form.save()

        AddUser = TeamMate.objects.create(team=self.object, user=self.request.user, admin=True)
        AddUser.save()

        return super(TeamCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('teams:TeamDetail', kwargs={'pk': self.object.id})


class InviteUser(CreateView):
    model = Invite
    form_class = InviteUserForm
    success_url = '/'

    def form_valid(self, form):
        TeamForm = form.save(commit=False)
        TeamForm.invite_from = self.request.user


        if owner(self, form.cleaned_data["team"].id):
            self.object = form.save()
        else:
            print "not owner"
            form.clean()
            
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
            if form.cleaned_data["accept"] == "Accept":
                try:
                    TeamMate.objects.create(team=inviteobject.team, user=inviteobject.invite_to, admin=False)
                except:
                    print "failed"


        return super(InviteResponse, self).form_valid(form)

