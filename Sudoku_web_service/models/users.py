import psycopg2
import json



class users(object):
    def __init__(self, conection_obj=None):

        self.conection= conection_obj
        self.reference_key=None
        self.message=None
        self.info_got=None
    def insert_new_user(self, data):

        self.conection.conectDb()
        self.conection.cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (data['name'], data['email'], data['password']))
        self.conection.cur.execute('SELECT Id FROM users where email=%s', (data['email'], ))
        self.reference_key=self.conection.cur.fetchone()[0]
        self.conection.disconectDb()
        self.message='inserted in users'
        print(self.message)
    
    def check_name(self, new_name):
        self.conection.conectDb()
        self.conection.cur.execute('SELECT Id FROM users where name=%s', (new_name,))
        if self.conection.cur.fetchone() ==None:
            self.conection.disconectDb()
            return True
        else:
            self.conection.disconectDb()
            print('username already taken')
            return False

    def check_email(self, new_email):
        self.conection.conectDb()
        self.conection.cur.execute('SELECT Id FROM users where email=%s', (new_email,))

        if self.conection.cur.fetchone() ==None:
            self.conection.disconectDb()
            return True
        else: 
            self.conection.disconectDb()
            print('email already used')
            return False

    def check_Id(self, Id):
        self.conection.conectDb()
        self.conection.cur.execute('SELECT Id FROM users where Id=%s', (Id, ))
        if self.conection.cur.fetchone()!=None:
            return True
        else:
            return False

    def get_userId_shallow(self, new_data, key):

        self.conection.conectDb()
        
        self.conection.cur.execute('SELECT Id FROM users where (name=%s or email=%s) ', (new_data[key], new_data[key]))
        

        self.info_got=self.conection.cur.fetchone()
        
        #print(self.info_got)
        self.conection.disconectDb()
        return(self.info_got)


    def get_userId_login(self, credentials):
        
      

        for key in credentials:
            if key!='password':
                identifier=key
        

        self.conection.conectDb()
        
        self.conection.cur.execute('SELECT Id FROM users where (name=%s or email=%s) and password=%s', (credentials[identifier], credentials[identifier], credentials['password']))
        

        self.info_got=self.conection.cur.fetchone()
        
        #print(self.info_got)
        self.conection.disconectDb()
        return(self.info_got)
    
    def update(self, userId, newInfo):

        print(newInfo)

        self.conection.conectDb()
        self.conection.cur.execute('UPDATE users SET name=%s, email=%s, password=%s where Id=%s', (newInfo['name'], newInfo['email'], newInfo['password'], userId))
        self.conection.disconectDb()
        self.message='information updated'
        print(self.message)

    def delete_user(self, userId):
        
        self.conection.conectDb()
        self.conection.cur.execute('DELETE FROM users where Id=%s', (userId, ))
        self.conection.disconectDb()
        self.message='user deleted'
        print(self.message)