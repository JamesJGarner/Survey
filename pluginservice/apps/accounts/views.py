from django.views.generic import FormView
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login

class CreateAccount(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']

        )

        if user is not None:
            if user.is_active:
                login(self.request, user)

        return super(CreateAccount, self).form_valid(form)

class ChangePassword(FormView):
    form_class = PasswordChangeForm
