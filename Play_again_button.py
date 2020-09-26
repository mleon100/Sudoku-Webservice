from tkinter import *
from Sudoku_toolbox_for_size_n import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os




class Play_again_button(object):
    def __init__ (self, master, button_operator=None):
        self.master_frame= master
        self.button_comand=button_operator
        self.button_object=None
    # def event_handler(self):
    #     self.button_command()
    def play_again_bcreator(self):

        self.button_object= Button(self.master_frame, fg='snow', bg='blue2', text='Play Again', command= self.button_comand)
        self.button_object.grid(row=2, column=0)