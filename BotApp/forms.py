from django import forms
from .models import Command

class cmdForm(forms.Form):
    command = forms.CharField(label="Command", max_length=100)

    def process(self):
        cd = self.cleaned_data
        cmd = Command(cmd=cd['command'])
        cmd.save()