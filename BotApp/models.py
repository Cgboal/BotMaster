from django.db import models

# Create your models here.

class Bot(models.Model):
    botId = models.CharField(max_length=32)
    botName = models.CharField(max_length=100)
    lastSeen = models.PositiveIntegerField()
    platform = models.CharField(max_length=200)

    def __str__(self):
        return self.botName

class Command(models.Model):
    cmd = models.CharField(max_length=100)
    botId = models.CharField(max_length=32)

    def __str__(self):
        return self.cmd