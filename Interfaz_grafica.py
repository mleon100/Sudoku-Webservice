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

    def __init__(self, master):

        self.entry_master=master
        self.entry_object=None
        self.num_entry_label=None
        self.enter_entry_button=None
        self.user_input=[]
        self.first_try=True
        self.valid_entry=None
        self.entry_counter=0

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
            self.user_input=[position_mapping(Gui.Sudoku.size,1)[int(Gui.clicked_button_list[n-1][1])][0], position_mapping(Gui.Sudoku.size,1)[int(Gui.clicked_button_list[n-1][1])][1], self.entry_object.get()]
            
            # prueba las reglas de sudoku, entrega booleano
            self.valid_entry= sudoku_rule_test_GUI(Gui.Sudoku, Gui.Sudoku.size,self.user_input)
            
            
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

                Gui.num_entry_frame.grid_remove()

                if self.entry_counter==Gui.Sudoku.dificulty_index:
                    Gui.victory_alarm=True
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

class Sudoku_Radbutton (object):

    def __init__(self, master):

        self.Rad_master=master
        self.R1=None
        self.R2=None
        self.R_none=None
        self.num_entry_frame=None

    def R1_command(self):
        
        Gui.num_entry_frame.grid(row=1, column=1)

        return()

    # boton de reseteo
    def R2_command(self):
        n= len(Gui.clicked_button_list)

        Gui.clicked_button_list[n-1][0]['text']= 'x'
        Gui.clicked_button_list[n-1][0]['fg']='black'
        Gui.clicked_button_list[n-1][0]['bg']='gray92'
        Gui.clicked_button_list[n-1][2]= 'x'
        self.R_none.select()
        self.R2.deselect()
        self.R1["state"]="disabled"
        self.R2["state"]="disabled"
        Gui.num_entry_frame.grid_remove()
    
    def Radiobutton_creator (self):
                
        '''
        creates a  where the user decides to either place 
        a number or reset the value of that position

        '''       

        master= self.Rad_master
        button_status= StringVar()
        
        # Radiobutton R_none is a non visible radiobutton created so that R1 an R2 may be both deselected at the same time.
        self.R_none= Radiobutton(master, text='none', state= DISABLED, variable= button_status, value='kkck' , command= lambda : print('kkck'))
        #self.R_none.pack()
        self.R_none.select()
        
        self.R1= Radiobutton(master,text='Place Number', bg='ghost white', state=DISABLED,variable=button_status, value= 'num inactive', command= lambda : self.R1_command())
        self.R1.deselect()
        #self.R1.pack(anchor=W)
        
              
        self.R2= Radiobutton(master, text='Reset Entry', bg='ghost white', pady=22, padx= 10, state=DISABLED, variable= button_status, value= 'reset inactive', command= lambda : self.R2_command())
        self.R2.deselect()
        self.R2.pack(anchor=W)
                      
        return() 

    def enable_rads(self):
        self.R_none["state"]="normal"
        self.R_none.select()
        #self.R1["state"]="normal"
        #self.R1.deselect()
        self.R2["state"]="normal"
        #self.R2.deselect()

        return()

   
    
    def disable_rads(self):

        #self.R1["state"]="disabled"
        self.R2["state"]="disabled"

        return()

class Sudoku_button (object):
       
    def __init__(self,master,value=1, position=1):

        self.master=master
        self.value=value
        self.position=position
        self.button_object=None
        self.first_click=True
        #self.valid_button= None
        
                     

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
            
            if Gui.clicked_button_list[n-1][0]['bg']=='RoyalBlue' :
                #print('azul pinchado')
                Gui.valid_button=True

        Gui.clicked_button_list[n-1][0]['bg']='gray62'

        # Condicion para crear un solo entry
        if n!=1:
            self.first_click=False

               
        #condicion para el primer boton pulsado en toda la partida
        if (self.position in Gui.Sudoku.get_editable_positions()) and (self.value=='x') and self.first_click:
            #print(self.value, self.position)
            num_entry= Sudoku_Num_Entry(Gui.num_entry_frame)
            num_entry.NUM_entry_creator()
            Gui.num_entry_frame.grid(row=1, column=1)
            self.first_click=False
               
            
        # llenar casilla con x       
        elif (self.position in Gui.Sudoku.get_editable_positions()) and (Gui.clicked_button_list[n-1][0]['text']=='x') and (not self.first_click):
            Gui.num_entry_frame.grid(row=1, column=1)
            if Gui.Rad_button.R2['state']=='normal':
                Gui.Rad_button.disable_rads()
        # resetear Casilla
        elif (self.position in Gui.Sudoku.get_editable_positions()) and (Gui.clicked_button_list[n-1][0]['text']!='x'):
            #print(self.value, self.position)
            #print('arrepentido')
            Gui.num_entry_frame.grid_remove()
            Gui.Rad_button.enable_rads()
        
        
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

class Sudoku_GUI(object):
      
    def __init__(self,size=9,root=None,S=None):
        
        self.root=root
        self.Sudoku=S
        #self.size= self.Sudoku.size
        self.button_matrix=None
        self.position_button_dict=None
        self.master_frame= Frame(root,bg='ghost white',bd=4)
        self.num_entry_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
        self.Rad_button=None
        self.clicked_button_list=[]
        self.valid_button=False
        self.victory_alarm=False
        self.clock_frame= Frame(self.master_frame, bd=2, bg= 'ghost white')
        self.timer=None
               
    def button_matrix_creator(self):
        '''
        S can be any variation of the square matrix sudoku
        oritinal, playable or solution.

        This method takes the matrix and generates a button for
        each position of the object sudoku

        And also registers each button to its corresponding position 
        (integer from 1 to size**2) in the matrix in atribute
        position_button_dict: KEYS= positions, VALUES= buttons
        '''
        
        master=self.master_frame
        size= self.Sudoku.size
        
        
        buttonmatrix_master_frame= Frame(master, bd=2, bg= 'MistyRose4')    
        m=int(size**0.5)
        frame_list=[]
                
        position_button_dict={}
        
        # submatrix frame creator
        for i in range(1,size+1,1):

            position_submatrix=sector_mapping(size)[i]
            frame_list.append(Frame(buttonmatrix_master_frame, bd=3, bg= 'MistyRose4'))

            # row
            for j in range(m):
                # col
                for k in range(m):
                    current_position=position_submatrix[j,k]
                    current_button= Sudoku_button(frame_list[i-1], self.Sudoku.playable[position_mapping(size,1)[current_position][0],position_mapping(size,1)[current_position][1]], current_position)
                    current_button.button_creator()
                    
                 
                    # storage of button position as buttons are creted
                    position_button_dict[current_position]=[current_button.value,current_button.button_object]
                    current_button.button_object.grid(row=j,column=k)
               
        # creates grid from the frame list
        i=0
        for j in range(m):
            for k in range(m):
                frame_list[i].grid(row=k, column=j)
                i=i+1

        self.button_matrix=buttonmatrix_master_frame
        self.position_button_dict=position_button_dict
        #self.button_matrix.pack(anchor= SW)
        self.button_matrix.grid(row=2,column=1)
        #self.button_matrix.place(anchor=SW)
          
        return()

    def Radbutton_init(self):

        #self.Upper_frame= Frame(self.master_frame, bd=2, bg='ghost white')
        Rads_frame= Frame(self.master_frame, bd=2, bg= 'ghost white') 
               
        self.Rad_button= Sudoku_Radbutton(Rads_frame)
        self.Rad_button.Radiobutton_creator()
   
        Rads_frame.grid(row=1,column=0)
        return()

   
    def Construct(self):
        
        self.timer= Sudoku_timer(self.clock_frame)
        self.clock_frame.grid(row=2, column=0)
        self.master_frame.pack()

        return()


root= Tk()

S=Sudoku(9,1)
size=S.size

Gui= Sudoku_GUI(size,root,S)
Gui.Radbutton_init()
Gui.button_matrix_creator()
Gui.Construct()

root.mainloop()