from tkinter import *
from Sudoku_toolbox_for_size_n import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os

class Sudkoku_menu_button(object):
    def __init__(self, master, save_command=None, surrender_command=None):
        self.menu_master_frame= master
        self.save_command=save_command
        self.surrender_command=surrender_command
        self.menu_bar=Menu(self.menu_master_frame)
        self.menu_object=None

    def menu_creator(self):

        self.menu_master_frame.config(menu=self.menu_bar)

        self.menu_object= Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Menu', menu=self.menu_object)
        self.menu_object.add_command(label='Save and Exit', command=lambda :self.save_command())
        self.menu_object.add_command(label='Surrender', command=lambda :self.surrender_command())

    def menu_remover(self):
        
        emptyMenu= Menu(self.menu_master_frame)
        self.menu_master_frame.config(menu=emptyMenu)