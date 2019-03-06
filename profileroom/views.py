import json

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse

def profile(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    return render(request, 'profileroom/index.pug')

def logout_profile(request):
    logout(request)
    data = 'OK'
    return HttpResponse(json.dumps(data))
