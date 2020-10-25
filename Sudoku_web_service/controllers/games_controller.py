import sys

sys.path.append('C:/Users/Mauricio León/Desktop/MAURICIO/PROGRAMACION/Sudoku-Webservice/Sudoku_web_service/models')

from games import games
from data_admin import conection_admin
from games_req_val import games_req_validator

db_admin= conection_admin()

games_db=games(db_admin)

games_validator= games_req_validator(games_db)

class games_controller(object):
    def __init__(self, db_object= games_db):

        self.games_db= db_object
    def save_game(self, userId, data):

        self.games_db.save_game(userId, data)
    def end_game(self, userId, data):

        self.games_db.end_game(userId, data)
    def load_info(self, game_name):

        return self.games_db.load_game(game_name)
    def show_user_games(self, userId):

        if games_validator.games_exist(userId):
            return self.games_db.retrieve_gamelist(userId)
        else:
            return 'user does not have any saved games'
    
    def show_single_game(self, gameId):

        if games_validator.single_game_exist(gameId):
            return self.games_db.retrieve_singlegame(gameId)
        else:
            return 'no game with such Id'
    
    def leaderboards(self):
        if games_validator.leaderboards_exist():
            return self.games_db.show_leaderboards()
        else:
            return 'no leaderboars'










