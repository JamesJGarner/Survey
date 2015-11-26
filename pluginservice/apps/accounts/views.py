from django.views.generic import FormView, UpdateView
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import UserCreateForm
from .models import UserProfile
from django.contrib.auth import authenticate, login

class CreateAccount(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreateForm
    success_url = '/'

    def form_valid(self, form):
        createform = form.save(commit=False)
        createform.username = form.cleaned_data['username'].lower()
        self.object = form.save()

        user = authenticate(
            username=form.cleaned_data['username'].lower(),
            password=form.cleaned_data['password1']
        )

        if user is not None:
            if user.is_active:
                login(self.request, user)

        return super(CreateAccount, self).form_valid(form)

class ChangePassword(FormView):
    form_class = PasswordChangeForm


class TutorialForm(FormView):
    template_name = 'accounts/register.html'
    success_url = '/'

    def form_valid(self, form):   
        user = UserProfile.get(user=self.request.user)
        user.tutorial_completed = True;
        user.save()


class UserProfileUpdate(FormView):
    model = UserProfile
