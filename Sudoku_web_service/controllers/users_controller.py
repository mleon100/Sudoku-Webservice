import sys
sys.path.append('C:/Users/Mauricio León/Desktop/MAURICIO/PROGRAMACION/Sudoku-Webservice/Sudoku_web_service/models')

from data_admin import conection_admin
from users import users
from user_req_val import user_req_validator

Db_access= conection_admin()

users_Db=users(Db_access)
user_validator= user_req_validator(users_Db)

class user_controller(object):
    def __init__(self, db_object=users_Db):
        
        self.users_db= db_object
    def create_new_user(self, data):

        if user_validator.val_new_user(data):
            #print('entra2')
            self.users_db.insert_new_user(data)
            return('user created succesfully')
        else:
            return('user could not be created')
        
    
    def delete_user(self, userId):
        if user_validator.val_delete_user(userId):
            self.users_db.delete_user(userId)
            return('user deleted succesfully')
        else:
            return('user could not be deleted')
        

    def update_user_info(self, userId, new_data):

        if user_validator.val_update_user(userId, new_data):
            self.users_db.update(userId, new_data)
            return('user info updated succesfully') 
        else:     
            return 'user info could not be updated'
        
        self.users_db.update(userId, new_data)
    def login(self, credentials):
        if user_validator.val_login_user(credentials):
            return {'userId': self.users_db.get_userId_login(credentials)}
        else:
            return ('failed to login')
         
    






