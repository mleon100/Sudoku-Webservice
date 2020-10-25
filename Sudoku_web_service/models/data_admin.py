import psycopg2
import json



class conection_admin(object):
    def __init__(self):
        self.conn=None
        self.cur=None

       

    def conectDb(self):
        self.conn=psycopg2.connect(host="localhost", database='User_game', user='postgres' , password="12345", port=5432)
        self.cur= self.conn.cursor()
    
    def disconectDb(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
    
    def createTables(self):
        self.conectDb()

        self.cur.execute('''

        DROP TABLE if exists users CASCADE;
        DROP TABLE if exists games CASCADE;
        DROP TABLE if exists incomplete_games;

        CREATE TABLE users(
            Id SERIAL NOT NULL PRIMARY KEY UNIQUE,
            name TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
            );

        CREATE TABLE games(
            Id SERIAL NOT NULL PRIMARY KEY UNIQUE,
            game_name TEXT UNIQUE,
            userId INTEGER REFERENCES users (Id),
            duration TEXT,
            difficulty INTEGER,
            size INTEGER,
            completed BOOL,
            time INTEGER
            );
        
        CREATE TABLE incomplete_games(
            gameId INTEGER REFERENCES games (Id),
            dificulty_index INT,
            s_entrycounter INT,
            s_start text,
            s_solution text,
            s_playable text
            );
        ''')
        self.disconectDb()

# A= conection_admin()
# A.createTables()







    

    



