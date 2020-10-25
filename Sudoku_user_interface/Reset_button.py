from tkinter import *
from Sudoku_toolbox_for_size_n import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os



class Reset_button(object):
    def __init__(self, master, reset_button_operator=None):
        self.Reset_button_master=master
        self.R_button_object=None
        self.button_event=False
        self.reset_button_operator= reset_button_operator
               
    def R_button_event_handler(self):
        self.button_event=True
        self.reset_button_operator()
           
    def R_button_creator(self):

        self.R_button_object= Button(self.Reset_button_master, text='RESET', bg='purple4', fg= 'snow', padx=5, state= DISABLED, command= lambda :self.R_button_event_handler())
            
    def enable_R_button(self):
                
        self.R_button_object['state']= 'active'
        self.R_button_object['bg']= 'purple1'
        self.R_button_object['activebackground']= 'purple1'
        self.R_button_object['activeforeground']= 'snow'
       

    def disable_R_button(self):
        
        self.R_button_object['state'] = 'disabled'
        self.R_button_object['bg']= 'purple4'
        self.R_button_object['activebackground'] = 'purple4'
        self.R_button_object['activeforeground'] = 'snow'
