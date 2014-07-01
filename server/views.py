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
from django_sse.redisqueue import RedisQueueView
from django_sse.redisqueue import send_event

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
    if request.method == 'GET':
        q = request.GET.get('term', '')
        songs = models.Song.objects.filter(Q(title__icontains = q)|Q(artist__icontains = q ))
        results = []
        for song in songs:
            song_json = {}
            song_json['id'] = song.id
            song_json['artist'] = song.artist
            song_json['title'] = song.title
            results.append(song_json)
        data = json.dumps(results)
        print data
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@login_required
def get_current_playlist(request):
    if request.method == 'GET':
        requests = models.Request.objects.all()
        results = []
        for request in requests:
            song_json = {}
            song_json['artist'] = request.song.artist
            song_json['title'] = request.song.title
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
        print id_song
        song = models.Song.objects.get(id=id_song)
        user = get_player(request.user)
        print user
        print song
        request = models.Request()
        request.user = user
        request.song = song
        request.priority = hotstuff.calc_priority_now(user.last_time_req)
        request.save()
        user.last_time_req = request.priority
        user.save()
        send_event('newsong', "ok", channel="foo")
        return HttpResponseRedirect("/playlist")
    elif request.method == 'GET':
        return render(request, 'server/request.html')

def get_next_song(request):
    if request.method == 'GET':
        try:
            now_request = models.Request.objects.get(now_play=True)
            now_request.delete()
        except:
            pass
        send_event('newsong', "ok", channel="foo")
        requests = models.Request.objects.order_by('priority')
        if requests:
            path = requests[0].song.path
            requests[0].now_play = True
            requests[0].save()
            return HttpResponse(json.dumps({'path':path}), 'application/json')
        #return HttpResponse(json.dumps({'status':'OK'}), 'application/json')
class SSE(RedisQueueView):
    def get_redis_channel(self):
        ch = self.redis_channel
        print ch
        return ch
