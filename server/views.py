from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from server import models
import json
import hotstuff
from django.db.models import Q

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
def search_songs(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        songs = models.Song.objects.filter(Q(title__icontains = q)|Q(artist__icontains = q ))
        results = []
        for song in songs:
            song_json = {}
            song_json['id'] = song.id
            song_json['label'] = song.title + ' ' + song.artist
            song_json['value'] = song.title + ' ' + song.artist
            results.append(song_json)
        data = json.dumps(results)
        print data
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

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

