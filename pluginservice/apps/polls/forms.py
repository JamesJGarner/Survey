from django import forms
from .models import Poll


class CreateForm(forms.ModelForm):
    choice1 = forms.CharField(required=False)
    choice2 = forms.CharField(required=False)
    choice3 = forms.CharField(required=False)

    class Meta:
        model = Poll
        exclude = ['created_by', 'deleted']
