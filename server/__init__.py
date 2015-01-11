import models

def create_player_after_login(strategy, user, response,
    is_new=False, *args, **kwargs):
    models.Player.objects.get_or_create(user=user)