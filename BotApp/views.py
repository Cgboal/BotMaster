from django.shortcuts import render
from .models import Bots

# Create your views here.
def index(request, botId=None, botName=None):
    if not botId and not botName:
        return render(request, 'index.html')
    bot = Bots(botId, botName)
    bot.save()
    return render(request, 'index.html')