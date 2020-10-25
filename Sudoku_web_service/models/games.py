import psycopg2
import json

class games(object):
    def __init__(self, conection_obj):

        self.conection= conection_obj
        #self.f_key= foreign_key
        self.message=None
        self.info_got=None

    #     self.initialize()
    
    # def initialize(self):
    #     self.connection.conectDb()
    #     self.connection.cur.execute('INSERT INTO games (userId) VALUES (%s)', (self.f_key,))
    #     self.connection.disconectDb()
    
    def save_game(self, userId, data):

        self.conection.conectDb()
        self.conection.cur.execute('INSERT INTO games (game_name, userId, duration, difficulty, size, completed, time) VALUES(%s, %s, %s, %s, %s, %s, %s)', (data['saved_name'], userId, data['time'], data['S_dificulty'], data['S_size'], False, data['abs_time']))
        self.conection.cur.execute('SELECT Id from games where userId= %s ', (userId, ))
        current_gameId= self.conection.cur.fetchone()
        self.conection.cur.execute('INSERT INTO incomplete_games(gameId, dificulty_index, s_entrycounter, s_start, s_solution, s_playable) VALUES (%s, %s, %s, %s, %s, %s)', (current_gameId, data['S_dificulty_index'], data['entry_counter'], data['S_start'], data['S_solution'], data['S_playable']))
        self.conection.disconectDb()


    
    def end_game(self, userId, data):

        self.conection.conectDb()
        self.conection.cur.execute('SELECT Id from games where game_name=%s', (data['saved_name'], ))
        current_gameId= self.conection.cur.fetchone()

        if current_gameId !=None:
            self.conection.cur.execute('UPDATE games SET duration=%s, completed=%s', (data['time'], True))
            self.conection.cur.execute('DELETE from incomplete_games where gameId=%s', (current_gameId, ))
            self.conection.disconectDb()
        else:
            self.conection.cur.execute('INSERT INTO games (game_name, userId, duration, difficulty, size, completed) VALUES(%s, %s, %s, %s, %s, %s)', (data['saved_name'], userId, data['time'], data['S_dificulty'], data['S_size'], True))
            self.conection.disconectDb()

    def load_game(self, game_name):

        self.conection.conectDb()
        self.conection.cur.execute('SELECT duration, difficulty, size, game_name, id from games where game_name=%s ', (game_name, ))
        games_info= self.conection.cur.fetchone()
        time= games_info[0]
        dificulty= games_info[1]
        size= games_info[2]
        g_name= games_info[3]
        gameId= games_info[4]
        
        self.conection.cur.execute('SELECT dificulty_index, s_entrycounter, s_start, s_solution, s_playable from incomplete_games where gameId=%s', (gameId, ))
        incomplete_g_info= self.conection.cur.fetchone()
        dif_index= incomplete_g_info[0]
        s_entrycounter= incomplete_g_info[1]
        s_start= incomplete_g_info[2]
        s_solution= incomplete_g_info[3]
        s_playable= incomplete_g_info[4]
        self.conection.disconectDb()

        load_data={'time': time, 'entry_counter': s_entrycounter, 'saved_name': g_name, 'S_size': size, 'S_start': s_start, 'S_solution' : s_solution, 'S_playable' : s_playable, 'S_dificulty' : dificulty, 'S_dificulty_index' : dif_index}
        return(load_data)

    def retrieve_gamelist(self, userId):
        self.conection.conectDb()
        self.conection.cur.execute('SELECT * from games where userId=%s', (userId, ))
        games= self.conection.cur.fetchall()
        self.conection.disconectDb()
        #print(games)
        game_register={}
        for i in range(len(games)):
            game_register[i+1]=games[i]

        return game_register
    
    def retrieve_singlegame(self, gameId):
        self.conection.conectDb()
        self.conection.cur.execute('SELECT * from games where Id=%s', (gameId, ))
        game= self.conection.cur.fetchone()
        self.conection.disconectDb()

        return {1:game}
    def show_leaderboards(self ):
        self.conection.conectDb()
        self.conection.cur.execute('SELECT * from games order by completed desc, size desc, difficulty desc, duration desc')
        leaderboards= self.conection.cur.fetchall()
        self.conection.disconectDb()
        leaderboards_regist={}
        if len(leaderboards)<10:
            it=len(leaderboards)-1
        else:
            it=10
        for i in range(it):
            leaderboards_regist[i+1]=leaderboards[i]
        
        return leaderboards_regist



        


        
    
    def insert(self, gameData):

        self.conection.conectDb()
        self.conection.cur.execute('INSERT INTO games (duration, difficulty, size, completed, date) VALUES (%s, %s, %s, %s, %s)', (gameData['duration'], gameData['difficulty'], gameData['size'], gameData['completed'], gameData['date']))
        self.conection.disconectDb()
        self.message='inserted in games'
        print(self.message)
    
    def get(self, gameId):

        self.conection.conectDb()
        self.conection.cur.execute('SELECT FROM games where gameId=%s', (gameId, ))
        self.info_got=self.conection.fetchone()
        self.conection.disconectDb()
        return(self.info_got)

    def update(self, gameId, newInfo):

        self.conection.conectDb()
        self.conection.cur.execute('UPDATE games SET duration=%s, dificulty=%s, size=%s, completed=%s, date=%s where gameId=%s', (newInfo['duration'], newInfo['dificulty'], newInfo['size'], newInfo['completed'], newInfo['date'], gameId))
        self.conection.disconectDb()
        self.message='games updated'
        print(self.message)

    def delete(self, gameId):

        self.conection.conectDb()
        self.conection.cur.execute('DELETE FROM games where gameId=%s', (gameId, ))
        self.conection.disconectDb()
        self.message='game deleted'
        print(self.message)