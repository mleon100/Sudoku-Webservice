from tkinter import *
from Sudoku_toolbox_for_size_n import *
from Reset_button import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os


class Sudoku_Num_Entry (object):

    def __init__(self, master, num_entry_operator=None, reset_button_operator=None, entry_conter=0):

        self.entry_master=master
        self.entry_object=None
        self.num_entry_label=None
        self.Reset_button=None
        self.reset_button_operator=reset_button_operator
        self.enter_entry_button=None
        self.label_spinbox_frame=Frame(self.entry_master, bd=2, bg= 'ghost white')
        self.Reset_Enter_frame=Frame(self.entry_master, bd=2, bg= 'ghost white')
        self.user_input=[]
        self.first_try=True
        self.valid_entry=None
        self.entry_counter=entry_conter
        self.victory_alarm=False
        self.Enter_button_event=False
        self.num_entry_operator=num_entry_operator

    def Num_entry_commamnd(self):
        # inicializacion de boton de entrada
        if self.first_try:
            self.enter_entry_button['state']='normal'
            self.enter_entry_button['bg']='forest green'
            self.first_try=False
        
        # validacion de input
        elif int(self.entry_object.get())>=1 or int(self.entry_object.get())<=9:
            self.enter_entry_button['bg']='forest green'
            self.enter_entry_button['text']='ENTER'

        return()

    def Enter_button_event_handler(self):
        self.Enter_button_event=True
        self.num_entry_operator()

    def enter_button_disable(self):
        self.enter_entry_button['bg']='gray25'
        self.enter_entry_button['state']='disabled'
    
    def enter_button_enable(self):
        self.enter_entry_button['state']='normal'
        self.enter_entry_button['bg']='forest green'
  
    def NUM_entry_creator(self):
        
        self.num_entry_label= Label(self.label_spinbox_frame , text= 'Ingresa AQUI un Numero: 1<=Num>=9', bg='ghost white', fg='blue2')
        self.num_entry_label.pack(anchor=NE)
        
        self.entry_object= Spinbox(self.label_spinbox_frame, from_=1, to=9, activebackground= 'forest green', disabledbackground= 'ghost white', disabledforeground= 'ghost white', command= lambda : self.Num_entry_commamnd())
        self.entry_object.pack(anchor=E)
        
        self.label_spinbox_frame.pack()

        self.Reset_button= Reset_button(self.Reset_Enter_frame, lambda : self.reset_button_operator())
        self.Reset_button.R_button_creator()
        self.Reset_button.R_button_object.grid(row=0, column=0)

        self.enter_entry_button=Button(self.Reset_Enter_frame, text='ENTER', bg= 'gray25', fg='ghost white', padx=5, state= DISABLED, command=lambda : self.Enter_button_event_handler())
        self.enter_entry_button.grid(row=0, column=1)

        self.Reset_Enter_frame.pack(anchor=E)

                
        return()