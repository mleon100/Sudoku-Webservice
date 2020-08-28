from tkinter import *
from Sudoku_toolbox_for_size_n import *
from sudoku_size_n import *
from Controller_size_n import *
import time

class Sudkoku_menu_button(object):
    def __init__(self, master, save_command=None, surrender_command=None):
        self.menu_master_frame= master
        self.save_command=save_command
        self.surrender_command=surrender_command
        self.menu_bar=Menu(self.menu_master_frame)
        self.menu_object=None

    def menu_creator(self):

        # self.menu_object= Menu(self.menu_master, activebackground='blue2', activeforeground='snow', bg='snow', fg='black')
        self.menu_master_frame.config(menu=self.menu_bar)

        self.menu_object= Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='MENU', menu=self.menu_object)
        self.menu_object.add_command(label='Save and Exit', command=lambda :self.save_command())
        self.menu_object.add_command(label='Surrender', command=lambda :self.surrender_command())

       

        
        



class Sudoku_timer(object):
    def __init__(self, master):
        self.clock_master=master
        self.ref_time=time.time()
        self.timer_display= Label(self.clock_master, bg='gray32', fg='snow', text= '00:00:00', padx=10)
        self.timer_display.pack()
        
        self.run_time()
              
    # recursive function, IMPORTANT, it is not invoking an instance when calling itself.
    def run_time(self):
        
        instant_time= time.time()
        seconds_passed= instant_time-self.ref_time
        self.timer_display['text']= time_format(seconds_passed)
        self.clock_master.after(1000, self.run_time)
        #print(time_format(seconds_passed))
                 
class Sudoku_Num_Entry (object):

    def __init__(self, master, num_entry_operator=None, reset_button_operator=None):

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
        self.entry_counter=0
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

class Sudoku_button (object):
       
    def __init__(self,master,value=1, position=1, on_click_handler=None):

        self.master=master
        self.value=value
        self.position=position
        self.button_object=None
        self.first_click=True
        self.clicked= False
        self.on_click_handler= on_click_handler
       
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
        if self.value!='x':
            self.button_object['state']='disabled'
        return()

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
                    current_button= Sudoku_button(frame_list[i-1], self.Sudoku.playable[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]], current_position, lambda : self.Button_event_handler())
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


class Sudoku_GUI(object):
      
    def __init__(self,size=9,root=None,S=None):
        
        self.root=root
        self.Sudoku=S
        self.button_matrix=None
        self.master_frame= Frame(root,bg='ghost white',bd=4)
        self.num_entry_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
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

            self.last_button[0]['bg']='gray62'

            # Condicion para crear un solo entry
            if self.penultimate_button!=None:
                self.first_click=False

               
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
            self.num_entry.Reset_button.disable_R_button()

    def num_entry_init(self):

        self.num_entry=Sudoku_Num_Entry(self.num_entry_frame, lambda : self.num_entry_operator(), lambda : self.Reset_button_operator())
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
                    self.last_button[0]['fg']='snow'
                    self.last_button[0]['bg']='RoyalBlue'
                   
                    if self.num_entry.entry_counter==self.Sudoku.dificulty_index:
                        self.num_entry.victory_alarm=True
                        print('GANASTE CTM!!!') 
    
    # def menu_save_command(self):
    #     pass

    def menu_init(self):

        self.menu= Sudkoku_menu_button(self.root)
        self.menu.menu_creator()
                     
    def Construct(self):
        
        self.num_entry_init()
        self.Button_matrix_init()
        self.menu_init()
        self.timer= Sudoku_timer(self.clock_frame)
        self.clock_frame.grid(row=0, column=1)
        self.master_frame.pack()

        return()
    

# root= Tk()
# root.title('SUDOKU GAME')
# #root.geometry('400x400')

# S=Sudoku(9,5)
# size=S.size

# Gui= Sudoku_GUI(size,root,S)

# Gui.Construct()


# root.mainloop()