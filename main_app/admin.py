from django.contrib import admin

# Register your models here.
from .models import Finch, Game
admin.site.register(Finch)
admin.site.register(Game)