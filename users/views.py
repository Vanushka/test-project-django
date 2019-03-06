import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def registration(request):
    return render(request, 'registration/index.pug')

def login(request):
    return render(request, 'login/index.pug')

def signup(request):
    data = json.loads(request.body.decode())
    # form to sign up is valid
    username = data['username']
    print(username, 'USERNAME')
    email = data['email']
    password = data['password']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.is_active=True
    user.save()
    data = 'OK'
    return HttpResponse(json.dumps(data))

def signin(request):
    data = json.loads(request.body.decode())
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        data = 'OK'
        return HttpResponse(json.dumps(data))
    else:
        # No backend authenticated the credentials
        data = 'Error'
        return HttpResponse(json.dumps(data))

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'login/index.pug')
