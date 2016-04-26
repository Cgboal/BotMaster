from django import forms
from .models import Command

class cmdForm(forms.Form):
    command = forms.CharField(label="Command", max_length=100)
    botId = forms.CharField(label="Bot ID", max_length=32, initial={'botId' : False})

    def process(self):
        cd = self.cleaned_data
        if not cd['botId']:
            cmd = Command(cmd=cd['command'], botId="*")
            cmd.save()
        else:
            cmd = Command(cmd=cd['command'], botId=cd['botId'])
            cmd.save()
