from django import forms
from .models import Invite


class InviteUserForm(forms.ModelForm):

	class Meta:
		model = Invite
		exclude = ['invite_from', 'closed']

class InviteResponseForm(forms.Form):
    invite_id =  forms.IntegerField()
    accept =  forms.CharField()
