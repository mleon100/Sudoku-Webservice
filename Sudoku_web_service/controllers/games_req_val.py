
class games_req_validator(object):
    def __init__(self, db_object=None):

        self.games_db= db_object
    
    def games_exist(self, userId):

        if len(self.games_db.retrieve_gamelist(userId))!=0:
            return True
        else:
            return False

    def single_game_exist(self, gameId):

        if self.games_db.retrieve_singlegame(gameId)[1] !=None:
            return True
        else:
            return False
    def leaderboards_exist(self):
        if len(self.games_db.show_leaderboards())>0:
            return True
        else:
            return False