import sys
sys.path.append('C:/Users/Mauricio León/Desktop/MAURICIO/PROGRAMACION/Sudoku-Webservice/Sudoku_web_service/controllers')
from flask import flask, jsonify, request
from users_controller import user_controller

class route_users(object):
    def __init__(self, API_object):

        self.app= API_object
