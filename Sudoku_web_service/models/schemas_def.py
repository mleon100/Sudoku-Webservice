from data_admin import conection_admin
import psycopg2

class incomplete (object):
    def __init__(self, db_object):

        self.conection= db_object

    def users(self):

        self.conection.conectDb()

        self.cur.execute('''
        
        ''')
    
