from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from django.apps import apps
from django.contrib.auth.models import User, Group
from django.utils.html import format_html

from main import models
from django.contrib.sites.models import Site

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)



@admin.register(models.HomePG)
class BotClientAdmin(ModelAdmin):
    list_display = (
        'title_ru', 

    )
