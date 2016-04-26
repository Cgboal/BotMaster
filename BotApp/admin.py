from django.contrib import admin
from .models import Bot, Command, Host

# Register your models here.
admin.site.register(Bot)
admin.site.register(Command)
admin.site.register(Host)