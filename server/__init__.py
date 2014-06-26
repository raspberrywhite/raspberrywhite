def create_player_after_login(strategy, user, response,
    is_new=False,*args,**kwargs):
    try:
        models.Player.objects.get(user=user)
    except:
        player = models.Player()
        player.user = user
        player.save()