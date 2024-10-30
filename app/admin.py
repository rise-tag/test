from django.contrib import admin

from django.contrib import admin
from apps.settings.models import Basesettings, Empty
# Register your models here.

admin.site.register(Basesettings)
admin.site.register(Empty)
