from django.db import models

# Create your models here.

class Bots(models.Model):
    botId = models.CharField(max_length=32)
    botName = models.CharField(max_length=100)

    def __str__(self):
        return self.botName