

class user_req_validator(object):
    def __init__(self, db_object=None):

        #self.request=request_obj
        self.users_db= db_object
        self.complete_data=False
        self.valid_req=False

    def validate(self):
        '''
        method for internal use only
        '''
        if self.complete_data and self.valid_req:
            self.complete_data=False
            self.valid_req=False
            return True
        else:
            self.complete_data=False
            self.complete_data=False
            return False

    def val_new_user(self, incoming_data):

        #incoming_data= self.request.get_json

        if 'name' and 'email' and 'password' in incoming_data:
            self.complete_data=True
        else:
            print('incomplete request')

        
        if self.users_db.check_name(incoming_data['name']) and self.users_db.check_email(incoming_data['email']):
            self.valid_req=True
        else:
            print('user information already taken')
        
        return self.validate()
    
    def val_delete_user(self, Id):

        #Id= self.request.get_json

        if Id!=None:
            self.complete_data=True
        else:
            print('incomplete request')

            
        
        if self.users_db.check_Id(Id):
            self.valid_req=True
        else:
            print('no such user')
        
        return self.validate()
        
    
    def val_update_user(self, userId, new_data):

        #new_data= self.request.get_json

        if ('name' and 'email' and 'password' in new_data) and (userId!=None):
            self.complete_data=True
        else:
            print('incomplete request')


        if self.users_db.check_Id(userId):
            print('userId found')

            name_Id= self.users_db.get_userId_shallow(new_data,'name')
            email_Id= self.users_db.get_userId_shallow(new_data,'email')

            if (name_Id!=None and email_Id!=None and name_Id!=email_Id) or (name_Id!=userId) or (email_Id!= userId):
                print('new information is conflicting with repo')
                self.valid_req= False
            else:
                self.valid_req=True

        else:
            print('need to be logged in')


        return self.validate()
        
     
    def val_login_user(self, credentials):

        #credentials= self.request
        
        if 'name' or 'email' and 'password' in credentials:
            self.complete_data=True
        else:
            print('incomplete request')


         
        if self.users_db.get_userId_login(credentials)!=None:
            self.valid_req=True
        else:
            print('no user with such credentials')
            
        return self.validate()

        

# con_admin= conection_admin()
# db_test= users(con_admin)       
# test= user_req_validator(db_test)

# new_d= {'name': 'nprueba1', 'email': 'gatuno@feino.org', 'password':'pasprueba1' }

# print(test.val_new_user(new_d))

# user=8
# print(test.val_delete_user(user))

# updatedinfo={"name": "guarrer", "email": "guarrete@elguarro.com", "password":"guarrino4"}
# userId=1
# print(test.val_update_user(userId, updatedinfo))
        


            
                


        
        
        


        




