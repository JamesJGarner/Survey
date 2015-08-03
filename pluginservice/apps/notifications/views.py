from django.views.generic import FormView
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login

def CreateNotifcation(to_user, text ):
    return text