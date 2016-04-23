from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bots

# Create your views here.
@csrf_exempt
def index(request):
    if 'botId' not in request.POST and 'botName' not in request.POST:
        return render(request, 'index.html')
    bot = Bots(request.POST['botId'], request.POST['botName'])
    bot.save()
    return render(request, 'index.html')