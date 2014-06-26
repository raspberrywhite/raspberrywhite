from views import create_player

def create_player_after_login(strategy, user, response,
    is_new=False,*args,**kwargs):
    create_player(user)