from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from apps.settings.models import Basesettings, Empty

def settings(request):
    setting = Basesettings.objects.latest('id')
    empty = Empty.objects.all().order_by("?")[:4]
    return render(request, 'index.html', locals())