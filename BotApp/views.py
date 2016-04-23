from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bots

# Create your views here.
@csrf_exempt
def index(request):
    bot = Bots(request.POST['botId'], request.POST['botName'])
    bot.save()
    return render(request, 'index.html')