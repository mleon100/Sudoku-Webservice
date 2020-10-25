from tkinter import *
from tkinter import W
from Sudoku_toolbox_for_size_n import *
from sudoku_size_n import *
import numpy as np

# print(sector_mapping(9))
# print(position_mapping(9,1))

def button_matrix(size,root,S):
    
    n=int(size**2)
    button_list=[]
    
    
    # button creator
    for i in range(n):
        matrix_value= str (S.playable[position_mapping(size,1)[i+1][0],position_mapping(size,1)[i+1][1]])
        #button_list.append(Button(root, text=S.playable(position_mapping(size,1)[i+1][0],position_mapping(size,1)[i+1][1])))
        button_list.append(Button(root, text=matrix_value, padx=4))    
    #button grid creator
    i=0
    for j in range(size):
        for k in range(size):
            button_list[i].grid(row=j, column=k)
            i=i+1


    

    return()
S=Sudoku()
root= Tk()
size=9
button_matrix(size,root,S)
root.mainloop()


    