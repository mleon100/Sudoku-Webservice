from tkinter import *
from Sudoku_toolbox_for_size_n import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os





class Sudoku_button (object):
       
    def __init__(self,master,value=1, position=1, on_click_handler=None, is_loaded=False):

        self.master=master
        self.value=value
        self.position=position
        self.button_object=None
        self.first_click=True
        self.clicked= False
        self.on_click_handler= on_click_handler
        self.is_loaded=is_loaded
       
    def Event_button_clicked(self):
        self.clicked=True
        self.on_click_handler()
       
    def Info_transporter(self):
        return([self.button_object, self.position, self.value])

     
    def button_creator (self):

        # Condicion para cuando size de sudoku es mayor a 9
        if len(str(self.value))>1:
                
            self.button_object=Button(self.master, text=self.value, bg='gray92', padx=2, command=lambda : self.Event_button_clicked())
        else:
            self.button_object=Button(self.master, text=self.value, bg='gray92', padx=5, command=lambda : self.Event_button_clicked())

        # Desactivar casillas no editables
        if self.value!='x' and  (not self.is_loaded):
            self.button_object['state']='disabled'

        elif self.is_loaded:
            #self.button_object['state']='active'
            self.button_object['fg']= 'snow'
            self.button_object['bg']= 'RoyalBlue'
           


        return()