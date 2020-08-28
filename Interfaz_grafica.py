from tkinter import *
from Sudoku_toolbox_for_size_n import *
from sudoku_size_n import *
from Controller_size_n import *
import time



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

    def __init__(self, master, Sudoku):

        self.entry_master=master
        self.Sudoku=Sudoku
        self.entry_object=None
        self.num_entry_label=None
        self.enter_entry_button=None
        self.user_input=[]
        self.first_try=True
        self.valid_entry=None
        self.entry_counter=0
        self.victory_alarm=False

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

    def info_input (self):

        # Validacion de input
        if int(self.entry_object.get())<1 or int(self.entry_object.get())>9:

            self.enter_entry_button['bg']='red2'
            self.enter_entry_button['text']='Invalid/RETRY'

                  
        
        else:
            self.enter_entry_button['bg']='forest green'
            self.enter_entry_button['text']='ENTER'

            n= len(Gui.clicked_button_list)
            # almacenamiento de imput instantaneo
            self.user_input=[position_mapping(self.Sudoku.size,1)[int(Gui.clicked_button_list[n-1][1])][0], position_mapping(self.Sudoku.size,1)[int(Gui.clicked_button_list[n-1][1])][1], self.entry_object.get()]
            
            # prueba las reglas de sudoku, entrega booleano
            self.valid_entry= sudoku_rule_test_GUI(self.Sudoku, self.Sudoku.size,self.user_input)
            
            
            #print(self.valid_entry)

            # actualizacion de sudoku
            if self.valid_entry:
                
                self.entry_counter=self.entry_counter+1
                n=len(Gui.clicked_button_list)
                Gui.clicked_button_list[n-1][0]['text']=str(self.user_input[2])
               
                Gui.clicked_button_list[n-1][2]= str(self.user_input[2])
                
                Gui.clicked_button_list[n-1][0]['fg']='snow'
                Gui.clicked_button_list[n-1][0]['bg']='RoyalBlue'
                #Gui.last_button_valid=True

                self.entry_master.grid_remove()

                if self.entry_counter==self.Sudoku.dificulty_index:
                    self.victory_alarm=True
                    print('GANASTE CTM!!!') 

          
        return()
    
    def NUM_entry_creator(self):
        
        self.num_entry_label= Label(self.entry_master, text= 'Ingresa AQUI un Numero: 1<=Num>=9', bg='ghost white', fg='blue2')
        #self.num_entry_label.place(anchor=NE)
        self.num_entry_label.pack(anchor=NE)


        #self.entry_object= Entry(self.entry_master, textvariable= entry_var)
        self.entry_object= Spinbox(self.entry_master, from_=1, to=9, activebackground= 'forest green', disabledbackground= 'ghost white', disabledforeground= 'ghost white', command= lambda : self.Num_entry_commamnd())
        self.entry_object.pack(anchor=E)

        self.enter_entry_button=Button(self.entry_master, text='ENTER', bg= 'gray25', fg='ghost white', padx=5, state= DISABLED, command=lambda : self.info_input())
        self.enter_entry_button.pack(anchor=E)

        
        return()

class Reset_button(object):
    def __init__(self, master):
        self.Reset_button_master=master
        self.R_button_object=None
        

    def R_button_command(self):
        n= len(Gui.clicked_button_list)

        Gui.clicked_button_list[n-1][0]['text']= 'x'
        Gui.clicked_button_list[n-1][0]['fg']='black'
        Gui.clicked_button_list[n-1][0]['bg']='gray92'
        Gui.clicked_button_list[n-1][2]= 'x'
        
        self.disable_R_button()
        
       
    def R_button_creator(self):

        self.R_button_object= Button(self.Reset_button_master, text='RESET', bg='purple4', fg= 'snow', pady= 5, padx=5, state= DISABLED, command= lambda :self.R_button_command())
        self.R_button_object.pack()
    
    def enable_R_button(self):
        #print('morado automatico')

        
        self.R_button_object['state']= 'active'
        self.R_button_object['bg']= 'purple1'
        self.R_button_object['activebackground']= 'purple1'
        self.R_button_object['activeforeground']= 'snow'
       

    def disable_R_button(self):
        #print('desactivar')

        self.R_button_object['state'] = 'disabled'
        self.R_button_object['bg']= 'purple4'
        self.R_button_object['activebackground'] = 'purple4'
        self.R_button_object['activeforeground'] = 'snow'





class Sudoku_button (object):
       
    def __init__(self,master,value=1, position=1, Sudoku=None, Reset_button=None, num_entry_frame=None):

        self.master=master
        self.Sudoku=Sudoku
        self.Reset_button=Reset_button
        self.num_entry_frame=num_entry_frame
        self.value=value
        self.position=position
        self.button_object=None
        self.first_click=True
        self.clicked= False
        
                     

    def button_command(self):
               
        # Registro de botones pulsados
        Gui.clicked_button_list.append([self.button_object, self.position, self.value])
        #Gui.clock.update_clock()
        
        # n-1 es el ultimo boton pulsado
        n=len(Gui.clicked_button_list) 
        # print('')  
        # print(Gui.valid_button) 

        # Condicion para marcar el boton actual y desmarcar botones pasados sin afectar las soluciones ya marcadas de azul    
        if n>1:
            
            if Gui.clicked_button_list[n-2][0]['bg']!='RoyalBlue' and (not Gui.valid_button):
                Gui.clicked_button_list[n-2][0]['bg']='gray92'
                #print('no azul')
            if Gui.valid_button and Gui.clicked_button_list[n-2][0]['text']!='x':
                #print('azul')
                Gui.clicked_button_list[n-2][0]['bg']='RoyalBlue'
                Gui.valid_button=False
            else:
               
                Gui.valid_button=False
            
            if self.button_object['bg']=='RoyalBlue' :
                #print('azul pinchado')
                Gui.valid_button=True

        self.button_object['bg']='gray62'

        # Condicion para crear un solo entry
        if n!=1:
            self.first_click=False

               
        # condicion para el primer boton pulsado en toda la partida
        if (self.position in self.Sudoku.get_editable_positions()) and (self.value=='x') and self.first_click:
            #print(self.value, self.position)
            num_entry= Sudoku_Num_Entry(self.num_entry_frame, self.Sudoku)
            num_entry.NUM_entry_creator()
            self.num_entry_frame.grid(row=1, column=1)
            self.first_click=False
               
            
        # llenar casilla con x       
        elif (self.position in self.Sudoku.get_editable_positions()) and (self.button_object['text']=='x') and (not self.first_click):
            self.num_entry_frame.grid(row=1, column=1)
            #if self.Reset_button.R_button_object['state']=='normal':
            self.Reset_button.disable_R_button()
        # resetear Casilla
        elif (self.position in self.Sudoku.get_editable_positions()) and (self.button_object['text']!='x'):
            #print(self.value, self.position)
            #print('arrepentido')
            self.num_entry_frame.grid_remove()
            self.Reset_button.enable_R_button()
        
        
        return()
     
    def button_creator (self):

        # Condicion para cuando size de sudoku es mayor a 9
        if len(str(self.value))>1:
                
            self.button_object=Button(self.master, text=self.value, bg='gray92', padx=2, command=lambda : self.button_command())
        else:
            self.button_object=Button(self.master, text=self.value, bg='gray92', padx=5, command=lambda : self.button_command())

        # Desactivar casillas no editables
        if self.value!='x':
            self.button_object['state']='disabled'
        return()

class Button_matrix(object):
    def __init__(self, master, Sudoku, Reset_button, num_entry_frame):
        self.Button_matrix_master=master
        self.Sudoku= Sudoku
        self.Reset_button=Reset_button
        self.num_entry_frame=num_entry_frame
        self.button_matrix_object=None
        #self.position_button_dict=None
        self.button_list=None

    def button_matrix_creator(self):
        #master=self.master_frame
        size= self.Sudoku.size
        
        
        buttonmatrix_master_frame= Frame(self.Button_matrix_master, bd=2, bg= 'MistyRose4')    
        m=int(size**0.5)
        frame_list=[]
                
        #position_button_dict={}
        
        # submatrix frame creator
        for i in range(1,size+1,1):

            position_submatrix=sector_mapping(size)[i]
            frame_list.append(Frame(buttonmatrix_master_frame, bd=3, bg= 'MistyRose4'))

            # row
            for j in range(m):
                # col
                for k in range(m):
                    current_position=position_submatrix[j,k]
                    current_button= Sudoku_button(frame_list[i-1], self.Sudoku.playable[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]], current_position,self.Sudoku, self.Reset_button, self.num_entry_frame)
                    current_button.button_creator()
                    
                 
                    # storage of button position as buttons are creted
                    #position_button_dict[current_position]=[current_button.value,current_button.button_object]
                    #self.button_list.append(current_button.button_object)
                    current_button.button_object.grid(row=j,column=k)
               
        # creates grid from the frame list
        i=0
        for j in range(m):
            for k in range(m):
                frame_list[i].grid(row=k, column=j)
                i=i+1

        self.button_matrix_object=buttonmatrix_master_frame
        #self.position_button_dict=position_button_dict
        #self.button_matrix.pack(anchor= SW)
        self.button_matrix_object.grid(row=2,column=1)
        #self.button_matrix.place(anchor=SW)

    # def get_button_list(self):
    #     return(self.button_list.copy())



class Sudoku_GUI(object):
      
    def __init__(self,size=9,root=None,S=None):
        
        self.root=root
        self.Sudoku=S
        #self.size= self.Sudoku.size
        self.button_matrix=None
        #self.position_button_dict=None
        self.master_frame= Frame(root,bg='ghost white',bd=4)
        self.num_entry_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
        self.Reset_button=None
        self.clicked_button_list=[]
        self.valid_button=False
        self.clock_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
        self.timer=None
               
 
    
    def Button_matrix_init(self):
        self.button_matrix= Button_matrix(self.master_frame, self.Sudoku, self.Reset_button, self.num_entry_frame)
        self.button_matrix.button_matrix_creator()

    def Reset_button_init(self):

        
        Reset_b_frame= Frame(self.master_frame, bd=20, bg= 'ghost white') 
               
        self.Reset_button= Reset_button(Reset_b_frame)
        self.Reset_button.R_button_creator()

        
        Reset_b_frame.grid(row=1,column=0)
        return()

   
    def Construct(self):

        self.Reset_button_init()
        self.Button_matrix_init()
        
        self.timer= Sudoku_timer(self.clock_frame)
        self.clock_frame.grid(row=2, column=0)
        self.master_frame.pack()

        return()


root= Tk()

S=Sudoku(9,1)
size=S.size

Gui= Sudoku_GUI(size,root,S)

Gui.Construct()

root.mainloop()