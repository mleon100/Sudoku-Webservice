from tkinter import *
from Sudoku_toolbox_for_size_n import *
from Sudoku_button import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os


class Button_matrix(object):
    def __init__(self, master, Sudoku, button_matrix_operator=None):
        self.Button_matrix_master=master
        self.Sudoku= Sudoku
        self.button_matrix_object=None
        self.position_Sudoku_button_dict={}
        self.clicked_button_data=None
        self.Button_event=False
        self.button_matrix_operator=button_matrix_operator
        

    def button_matrix_creator(self):
        
        size= self.Sudoku.size
        buttonmatrix_master_frame= Frame(self.Button_matrix_master, bd=2, bg= 'MistyRose4')    
        m=int(size**0.5)
        frame_list=[]
                
        # submatrix frame creator
        for i in range(1,size+1,1):

            position_submatrix=sector_mapping(size)[i]
            frame_list.append(Frame(buttonmatrix_master_frame, bd=3, bg= 'MistyRose4'))

            # row
            for j in range(m):
                # col
                for k in range(m):
                    current_position=position_submatrix[j,k]
                    if self.Sudoku.playable[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]]== self.Sudoku.start[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]]:
                        #print('same')
                        current_button= Sudoku_button(frame_list[i-1], self.Sudoku.playable[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]], current_position, lambda : self.Button_event_handler(), False)
                    else:
                        #print('diferent')
                        current_button= Sudoku_button(frame_list[i-1], self.Sudoku.playable[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]], current_position, lambda : self.Button_event_handler(), True)

                    current_button.button_creator()
                                     
                    # storage of button position as buttons are creted
                    self.position_Sudoku_button_dict[current_position]=current_button
                    current_button.button_object.grid(row=j,column=k)
               
        # creates grid from the frame list
        i=0
        for j in range(m):
            for k in range(m):
                frame_list[i].grid(row=k, column=j)
                i=i+1

        self.button_matrix_object=buttonmatrix_master_frame
        self.button_matrix_object.grid(row=2,column=1)
     
    def Button_event_handler(self):
        
        for position in self.position_Sudoku_button_dict:
           
            if self.position_Sudoku_button_dict[position].clicked:
                
                self.Button_event=True
                self.clicked_button_data=self.position_Sudoku_button_dict[position].Info_transporter()
                self.position_Sudoku_button_dict[position].clicked=False
                self.button_matrix_operator()

    def Button_matrix_info_passer(self):
        return(self.clicked_button_data)