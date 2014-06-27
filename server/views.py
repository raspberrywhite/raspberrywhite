from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from server import models
import hotstuff

def create_player(user):
    try:
        models.Player.objects.get(user=user)
    except:
        player = models.Player()
        player.user = user
        player.save()

def get_player(user):
    try:
        return models.Player.objects.get(user=user)
    except:
        pass

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            create_player(user)
            auth.login(request, user)
            return HttpResponseRedirect("/playlist")
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
            create_player(user)
        return render(request, 'server/login.html')
    return render(request, 'server/register.html')

@login_required
def playlist(request):
    return render(request, 'server/playlist.html')

@login_required
def songrequest(request):
    if request.method == 'POST':
        id_song = request.POST.get('id_song', 123)
        song = models.Song.objects.get(id=id_song)
        user = get_player(request.user)
        request = models.Request()
        request.user = user
        request.song = song
        request.priority = hotstuff.calc_priority_now(user.last_time_req)
        request.save()
        user.last_time_req = request.priority
        user.save()
        return HttpResponseRedirect("/playlist")
    elif request.method == 'GET':
        return render(request, 'server/request.html')

