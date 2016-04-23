from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bots

# Create your views here.
@csrf_exempt
def index(request):
    botId = request.POST.get('botId', False)
    botName = request.POST.get('botName', False)
    if not botId and not botName:
        return render(request, 'index.html')
    bot = Bots(request.POST.get('botId'), request.POST['botName'])
    bot.save()
    return render(request, 'botAdded.html')