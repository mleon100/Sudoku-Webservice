import sys
sys.path.append('C:/Users/Mauricio León/Desktop/MAURICIO/PROGRAMACION/Sudoku-Webservice/Sudoku_logic/')

from tkinter import *
from Play_again_button import *
from Button_matrix import *
from Sudoku_button import *
from Reset_button import *
from Sudoku_Num_Entry import *
from Sudoku_menu_button import *
from Sudoku_timer import *
import datetime
import time
import json
import os



from Sudoku_toolbox_for_size_n import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *

       

#print(datetime.datetime.now())



class Sudoku_GUI(object):
      
    def __init__(self,size=9,root=None,S=None, saved_time=0,entry_counter=0, saved_name=None, play_again_command=None):
        
        self.root=root
        self.Sudoku=S
        self.button_matrix=None
        self.master_frame= Frame(root,bg='ghost white',bd=4)
        self.num_entry_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
        self.saved_entry_counter=entry_counter
        self.Reset_button=None
        self.menu=None
        self.clicked_button_list=[]
        self.valid_button=False
        self.clock_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
        self.timer=None
        self.active_button_info=None
        self.last_button=None
        self.penultimate_button=None
        self.first_click= True
        self.surrender_window=None
        self.surrender_frame= Frame(self.root, bd=2, bg= 'snow')
        self.solution_buttonmatrix_master_frame= Frame(self.surrender_frame, bd=2, bg= 'snow')
        self.storage_data={}
        self.save_name=None
        self.enter_name_entry=None
        self.saving_window=None
        self.saved_time=saved_time
        #self.directory='Saved_sudoku_games'
        self.path="C:/Users/Mauricio León/AppData/Local/Temp/Saved_sudoku_games/"
        self.end_game_buttons_frame=Frame(self.root, bd=2, bg= 'snow')
        #os.mkdir(path + directory)
        self.play_again_command= play_again_command
        self.end_game_register= {} 
        self.saved_name=saved_name
        
         
    def Button_matrix_init(self):

        self.button_matrix= Button_matrix(self.master_frame, self.Sudoku, lambda : self.Button_matrix_operator())
        self.button_matrix.button_matrix_creator()

    def Button_matrix_operator(self):
       
        if self.button_matrix.Button_event:
            
            self.last_button= self.button_matrix.Button_matrix_info_passer()
            self.button_matrix.Button_event=False
                   
       
            # Condicion para marcar el boton actual y desmarcar botones pasados sin afectar las soluciones ya marcadas de azul    
            if self.penultimate_button!=None:
                
                if self.penultimate_button[0]['bg']!='RoyalBlue' and (not self.valid_button):
                    self.penultimate_button[0]['bg']='gray92'
                    #print('no azul')
                if self.valid_button and self.penultimate_button[0]['text']!='x':
                    #print('azul')
                    self.penultimate_button[0]['bg']='RoyalBlue'
                    self.valid_button=False
                else:
                    self.valid_button=False
                if self.last_button[0]['bg']=='RoyalBlue' :
                    #print('azul pinchado')
                    self.valid_button=True


            # Condicion para juego cargado y primer boton pulsado es cassilla llena 
            if self.last_button[0]['bg']=='RoyalBlue' and self.penultimate_button==None:
                                
                self.valid_button=True

            self.last_button[0]['bg']='gray62'

            # Condicion para crear un solo entry
            if self.penultimate_button!=None:
                self.first_click=False
            
        
            # condicion para un juego cargado 
            if self.saved_time!=0:
                self.first_click=False
                self.num_entry_frame.grid(row=1, column=1)

               
            # condicion para el primer boton pulsado en toda la partida
            if (self.last_button[1] in self.Sudoku.get_editable_positions()) and (self.last_button[2]=='x') and self.first_click:
                            
                self.num_entry_frame.grid(row=1, column=1)
                self.first_click=False
               
            
            # llenar casilla con x       
            elif (self.last_button[1] in self.Sudoku.get_editable_positions()) and (self.last_button[0]['text']=='x') and (not self.first_click):
                
                self.num_entry.enter_button_enable()
                self.num_entry.Reset_button.disable_R_button()

            # resetear Casilla
            elif (self.last_button[1] in self.Sudoku.get_editable_positions()) and (self.last_button[0]['text']!='x'):
                
                self.num_entry.enter_button_disable()
                self.num_entry.Reset_button.enable_R_button()
            
            self.penultimate_button= self.last_button.copy()

   
    def Reset_button_operator(self):
        if self.num_entry.Reset_button.button_event:
            
            self.num_entry.Reset_button.button_event=False
            self.last_button[0]['text']= 'x'
            self.last_button[0]['fg']='black'
            self.last_button[0]['bg']='gray92'
            self.last_button[2]= 'x'
            self.num_entry.entry_counter=self.num_entry.entry_counter-1

            # resetea self.Sudoku.playable
            self.Sudoku.erase_entry(position_mapping(self.Sudoku.size,1)[self.last_button[1]][0], position_mapping(self.Sudoku.size,1)[self.last_button[1]][1])
            # print('')
            # print(self.Sudoku.get_playable())

            self.num_entry.Reset_button.disable_R_button()

    def num_entry_init(self):

        self.num_entry=Sudoku_Num_Entry(self.num_entry_frame, lambda : self.num_entry_operator(), lambda : self.Reset_button_operator(), self.saved_entry_counter )
        self.num_entry.NUM_entry_creator()
        

    def num_entry_operator(self):

        if self.num_entry.Enter_button_event:
            self.num_entry.Enter_button_event= False

            # Validacion de input
            if int(self.num_entry.entry_object.get())<1 or int(self.num_entry.entry_object.get())>9:

                self.num_entry.enter_entry_button['bg']='red2'
                self.num_entry.enter_entry_button['text']='Invalid/RETRY'
        
            else:

                self.num_entry.enter_entry_button['bg']='forest green'
                self.num_entry.enter_entry_button['text']='ENTER'

                
                # almacenamiento de imput instantaneo
                self.num_entry.user_input=[position_mapping(self.Sudoku.size,1)[int(self.last_button[1])][0], position_mapping(self.Sudoku.size,1)[int(self.last_button[1])][1], self.num_entry.entry_object.get()]
            
                # prueba las reglas de sudoku, entrega booleano
                self.num_entry.valid_entry= sudoku_rule_test_GUI(self.Sudoku, self.Sudoku.size,self.num_entry.user_input)
            
                # actualizacion de sudoku
                if self.num_entry.valid_entry:
                    
                    self.num_entry.entry_counter=self.num_entry.entry_counter+1
                    self.last_button[0]['text']=str(self.num_entry.user_input[2])
                    self.last_button[2]= str(self.num_entry.user_input[2])
                    self.last_button[2]= str(self.num_entry.user_input[2])
                    self.last_button[0]['fg']='snow'
                    self.last_button[0]['bg']='RoyalBlue'

                    #print(self.num_entry.user_input[0], self.num_entry.user_input[1], self.num_entry.user_input[2])
                    # print('')
                    # print(self.Sudoku.get_playable())
                    # print('')

                    self.Sudoku.place_num(self.num_entry.user_input[0], self.num_entry.user_input[1], self.num_entry.user_input[2])
                    # print(self.Sudoku.get_playable())

                   
                    if self.num_entry.entry_counter==self.Sudoku.dificulty_index:
                        self.num_entry.victory_alarm=True
                        self.menu.menu_remover()
                        last_buttons_frame= Frame(self.master_frame)

                        Label(last_buttons_frame, bg='snow', fg='forest green', text= 'You WON!!', padx=10).grid(row=0, column=1 )
                        Label(last_buttons_frame, bg='gray32', fg='snow', text= time_format(self.timer.seconds_passed), padx=10).grid(row=1, column=1 )

                        play_again_b= Play_again_button(last_buttons_frame, self.play_again_command)
                        play_again_b.play_again_bcreator()
                        quit_button= Button(last_buttons_frame, fg='snow', bg='red2', text='Quit', padx=20, command=self.root.destroy)
                        quit_button.grid(row=2, column=2)
                        last_buttons_frame.grid(row=4, column=1)
                                        


                        self.end_game_register['time']= time_format(self.timer.seconds_passed)
                        self.end_game_register['S_dificulty']= int(self.Sudoku.dificulty)
                        self.end_game_register['S_size']= int(self.Sudoku.size)
                        #print(str(datetime.datetime.now()))
                        game_signature=str(int(time.time()))

                         # game has been saved previously or not
                        if self.saved_time != 0:
                            self.end_game_register['saved_name']= self.saved_name
                        else:
                            self.end_game_register['saved_name']= game_signature

                        # en este punto se debe conectar con la ruta de end_game
                        
                        with open(self.path + game_signature + '.json', 'w',) as FILE:
                            json.dump(self.end_game_register, FILE)
                        
                        
                        
                        #print('GANASTE CTM!!!') 
    
    def menu_save_command(self):

        
        self.storage_data['time']=self.timer.seconds_passed
      

        S_start=list(self.Sudoku.get_original().flatten())
        S_solution=list(self.Sudoku.get_solution().flatten())
        S_playable=list(self.Sudoku.get_playable().flatten())
        S_size=int(self.Sudoku.size)
        S_dificulty=int(self.Sudoku.dificulty)
        S_dificulty_index=int(self.Sudoku.dificulty_index)

        self.storage_data['S_start']=S_start
        self.storage_data['S_solution']=S_solution
        self.storage_data['S_playable']=S_playable
        self.storage_data['S_size']=S_size
        self.storage_data['S_dificulty']=S_dificulty
        self.storage_data['S_dificulty_index']=S_dificulty_index
        self.storage_data['entry_counter']=self.num_entry.entry_counter
        self.storage_data['abs_time']= int (time.time())

               

      
        self.saving_window= Toplevel()
        self.saving_window.minsize(300,100)
        self.saving_window.title('Save Game')

        Label(self.saving_window, text='Provide a name to create a new file').pack()
        self.enter_name_entry= Entry(self.saving_window)
        self.enter_name_entry.pack()

        
        enter_button= Button(self.saving_window, text='ENTER', bg='blue2', fg='snow', command= lambda :self.menu_save_support_function())
        enter_button.pack()
              

    def menu_save_support_function(self):

        
        try:
            os.mkdir(self.path)
        except:
            pass

        self.save_name= self.enter_name_entry.get()
        self.storage_data['saved_name']= self.enter_name_entry.get()
        
        with open(self.path + self.save_name + '.json', 'w',) as FILE:
            json.dump(self.storage_data, FILE)

        self.saving_window.withdraw()
        self.root.destroy()

        #print(self.save_name)
    
    def menu_surrender_command(self):
        self.surrender_window= Toplevel()
        self.surrender_window.title('Surrender')
        

        size= self.Sudoku.size
        
        m=int(size**0.5)
        frame_list=[]
                
        # submatrix frame creator
        for i in range(1,size+1,1):

            position_submatrix=sector_mapping(size)[i]
            frame_list.append(Frame(self.solution_buttonmatrix_master_frame, bd=3, bg= 'MistyRose4'))

            # row
            for j in range(m):
                # col
                for k in range(m):
                    current_position=position_submatrix[j,k]
                    if current_position in self.Sudoku.get_editable_positions():
                        current_button= Button(frame_list[i-1], text= str(self.Sudoku.solution[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]]), bg='red2' , fg='snow', padx=5)
                    else:
                        current_button= Button(frame_list[i-1], text= str(self.Sudoku.solution[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]]), padx=5)
                              
                    current_button.grid(row=j,column=k)
               
        # creates grid from the frame list
        i=0
        for j in range(m):
            for k in range(m):
                frame_list[i].grid(row=k, column=j)
                i=i+1
        
        Label(self.surrender_window, text= 'Are You Sure You Want to SURRENDER?').pack()
        Button(self.surrender_window, text= 'SURRENDER', bg='red2', fg='snow', command= self.surrender_button_command).pack()
       

    def surrender_button_command(self):

        self.solution_buttonmatrix_master_frame.pack()
        self.master_frame.pack_forget()
        self.surrender_window.withdraw()
        #end_game_buttons_frame= Frame(self.root, bd=2, bg= 'snow')

        self.surrender_frame.pack()

        play_again_b= Play_again_button(self.end_game_buttons_frame, self.play_again_command)
        play_again_b.play_again_bcreator()
        quit_button= Button(self.end_game_buttons_frame, fg='snow', bg='red2', text='Quit', padx=20, command=self.root.destroy)
        quit_button.grid(row=2, column=1)
        self.end_game_buttons_frame.pack()

        # desactivar menu
        #self.menu.menu_bar.entryconfig(1 ,state='disabled')
        self.menu.menu_remover()
              

    def menu_init(self):

        self.menu= Sudkoku_menu_button(self.root, lambda : self.menu_save_command(), lambda :self.menu_surrender_command())
        self.menu.menu_creator()
   
    def Construct(self):
        
        self.num_entry_init()
        self.Button_matrix_init()
        self.menu_init()

        if self.saved_time!=0:
            self.timer=Sudoku_timer(self.clock_frame,True, self.saved_time)
        else:
                       
            self.timer= Sudoku_timer(self.clock_frame)
        self.clock_frame.grid(row=0, column=1)
        self.master_frame.pack()

        return()
    def S_revomve(self):
        self.master_frame.destroy()
        try:
            self.surrender_frame.destroy()
            self.end_game_buttons_frame.destroy()
        except:
            pass

    

# root= Tk()
# root.title('SUDOKU GAME')
# #root.geometry('400x400')

# S=Sudoku(9,1)
# size=S.size

# Gui= Sudoku_GUI(size,root,S)

# Gui.Construct()


# root.mainloop()