from tkinter import *
from Interfaz_graficaV2 import *

class start_screen(object):
    def __init__(self, master):
        self.root=master
        self.start_screen_masterframe= Frame(master, bg= 'black', height=400)
        self.screen_1_frame=Frame(self.start_screen_masterframe, bg='black', height=400)
        self.screen_2_frame=Frame(self.start_screen_masterframe, bg='snow', height=400)
        self.title_label=None
        self.new_game_button=None
        self.load_game_button=None
        self.leaderboard_button=None
        self.dificulty_slider=None
        self.size_spinbox=None
        self.start_game_button=None
        self.sudoku_dificulty=None
        self.sudoku_size=None

        self.Sudoku_Gui=None
        # self.slave_game=slave_game
        # self.game_constriction_command= game_constriction_command
    
    def screen_1_creator(self):

        self.title_label= Label(self.screen_1_frame, text='SUDOKU', fg= 'snow', bg='black')
        self.title_label.grid(row=0)

        self.new_game_button= Button(self.screen_1_frame, text='New Game', bg='blue2', fg='snow', command=lambda : self.new_game_button_command())
        self.new_game_button.grid(row=3)

        self.load_game_button= Button(self.screen_1_frame, text='Load Game', bg='blue2', fg='snow', state= DISABLED)
        self.load_game_button.grid(row=5)

        self.leaderboard_button= Button(self.screen_1_frame, text='Leaderboard', bg='blue2', fg='snow', state= DISABLED)
        self.leaderboard_button.grid(row=7)

        self.screen_1_frame.pack()
    
    def screen_2_creator(self):

        #dificulty= IntVar()
        Label(self.screen_2_frame, text='Select a Dificulty (1 is the easiest)').pack()

        self.dificulty_slider= Scale(self.screen_2_frame, bg= 'snow', fg= 'black', from_=1, to= 10, orient=HORIZONTAL, length=200)
        self.dificulty_slider.pack()

        Label(self.screen_2_frame, text='Choose the size of your sudoku (sudoku grid= size x size)').pack()
        self.size_spinbox= Spinbox(self.screen_2_frame, fg= 'black', values=(4,9,16,25,36))
        self.size_spinbox.pack()

        self.start_game_button= Button(self.screen_2_frame, bg='forest green', text='START GAME', fg='snow', command= lambda : self.start_game_button_command())
        self.start_game_button.pack()

    
    def new_game_button_command(self):
        
        self.screen_1_frame.pack_forget()
        self.screen_2_creator()
        self.screen_2_frame.pack()
    
    def start_game_button_command(self):

        self.sudoku_dificulty= int(self.dificulty_slider.get())
        self.sudoku_size= int(self.size_spinbox.get())

        #print(self.sudoku_dificulty, self.sudoku_size)
        self.screen_2_frame.pack_forget()
        self.start_screen_masterframe.pack_forget()

        self.Sudoku_Gui= Sudoku_GUI(self.sudoku_size, self.root, Sudoku(self.sudoku_size,self.sudoku_dificulty))
        self.Sudoku_Gui.Construct()


   
    def start_screen_constructor(self):

        self.screen_1_creator()
        self.start_screen_masterframe.pack()

        

root= Tk()

ST= start_screen(root)
ST.start_screen_constructor()


root.mainloop()