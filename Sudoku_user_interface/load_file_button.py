from tkinter import *
import os
import json
import numpy as np
from Interfaz_grafica import *
from Sudoku_load import *




class load_file_button(object):
    def __init__(self, master=None, filename=None, button_command=None, list_index=None):

        self.master_frame=master
        self.name= filename
        self.button_command= button_command
        self.list_index=list_index
        self.button_object=None

    # def event_handler(self):
        
        
    def file_button_creator(self):

        self.button_object= Button(self.master_frame, bg='black', fg='snow', text=str(self.name), command= lambda :self.button_command(self.list_index))
        self.button_object.pack()
