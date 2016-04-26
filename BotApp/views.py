from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bot
import time, hashlib

# Create your views here.
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def reg(request):
    botId = request.POST.get('botId', False)
    botName = request.POST.get('botName', False)
    auth = request.POST.get('auth', False)
    botPlat = request.POST.get('platform', False)
    t = request.POST.get('t', False)
    if botId and botName and botPlat and t and auth == genTimeSeed():
        if not Bot.objects.filter(botId=botId):
            bot = Bot(botId=botId, botName=botName, lastSeen=t, platform=botPlat)
            bot.save()
            return render(request, 'botAdded.html')
    return render(request, 'index.html')




def genTimeSeed():
    seed = roundDown(int(time.time()), 3)
    return hashlib.md5(str(seed)).hexdigest()

def roundDown(num, factor):
    return num - (num%factor)