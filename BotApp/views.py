from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bots
import time, hashlib

# Create your views here.
@csrf_exempt
def index(request):
    botId = request.POST.get('botId', False)
    botName = request.POST.get('botName', False)
    auth = request.POST.get('auth', False)
    if not botId or not botName or not auth:
        return render(request, 'index.html')
    elif auth != genTimeSeed():
        return render(request, 'index.html')
    bot = Bots(botId=botId, botName=botName)
    bot.save()
    return render(request, 'botAdded.html')

def genTimeSeed():
    seed = roundDown(int(time.time()), 5)
    return hashlib.md5(str(seed)).hexdigest()

def roundDown(num, factor):
    return num - (num%factor)