from django import forms
from .models import Poll


class CreateForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_by']
