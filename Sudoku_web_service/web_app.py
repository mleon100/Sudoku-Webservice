import sys
sys.path.append('C:/Users/Mauricio León/Desktop/MAURICIO/PROGRAMACION/Sudoku-Webservice/Sudoku_web_service/controllers')

from flask import Flask, jsonify, request
from users_controller import user_controller
from games_controller import games_controller




app= Flask(__name__)

user_cont= user_controller()
games_cont= games_controller()

@app.route('/users', methods=['POST'])
def new_user():
    ''' 
    user_info contains name, emai, and password
    '''
  
    # crete new user
    if request.method =='POST':

        return user_cont.create_new_user(request.json)
      


@app.route('/users/<int:userId>', methods=['PUT'])
def update_user(userId):
    
    # update existing user's info
    if request.method == 'PUT':
        return user_cont.update_user_info(userId, request.json)


@app.route('/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):

    # delete user from db     
    if request.method == 'DELETE':
        return user_cont.delete_user(userId)

       
            
@app.route('/user_login', methods=['POST'])
def login_user():

    # login    
    if request.method == 'POST':
        return user_cont.login(request.json)









@app.route('/games/<int:userId>', methods=['POST'])
def save_game(userId):

    if request.method== 'POST':
        games_cont.save_game(userId, request.json)

        return 'game saved'

@app.route('/games_end/<int:userId>', methods=['POST'])
def end_game(userId):

    if request.method=='POST':

        games_cont.end_game(userId, request.json)
        
        return('game ended')

@app.route('/games_load/<string:saved_name>', methods=['GET'])
def load_game(saved_name):
    
    if request.method== 'GET':
        return games_cont.load_info(saved_name)

@app.route('/game_list/<int:userId>', methods=['GET'])
def get_gamelist(userId):

    if request.method=='GET':
        return games_cont.show_user_games(userId)


# se podria tambien agregar userId como argumnto para asegurarnos que e juego pertenece al usuario
@app.route('/game_select/<int:gameId>', methods=['GET'])
def get_game(gameId):

    if request.method == 'GET':
        return games_cont.show_single_game(gameId)

@app.route('/game_leaderboards', methods=['GET'])
def get_leaderboards():
    if request.method == 'GET':
        return games_cont.leaderboards()





       


if __name__== '__main__':
    app.run(debug=True)