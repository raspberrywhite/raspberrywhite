from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/account/loggedin/")
        else:
            return HttpResponseRedirect("/account/invalid/")
    return render(request, 'server/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            User.objects.get(username=username)
        except:
            user = User.objects.create_user(username=username,
                                    password=password)
            user.save()
    return render(request, 'server/register.html')