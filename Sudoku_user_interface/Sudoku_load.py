import sys
sys.path.append('C:/Users/Mauricio León/Desktop/MAURICIO/PROGRAMACION/Sudoku-Webservice/Sudoku_logic/')
from Sudoku_toolbox_for_size_n import *
from Mformat_size_n import matrix_format




class Sudoku_load(object):
    def __init__(self,loaded_data=None):
        #self.sudoku= sudoku_creator(size,dificulty)
        self.start= loaded_data[0]
        self.solution= loaded_data[1]
        self.playable= loaded_data[2]
        self.size=loaded_data[3]
        self.dificulty=loaded_data[4]
        self.dificulty_index=loaded_data[5]
        self.editable_positions=[]
    
    def get_editable_positions(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.solution[i,j]!=self.start[i,j]:
                    self.editable_positions.append(position_mapping(self.size,0)[i,j])
        return(self.editable_positions.copy())

        
    
    def reset_dificulty(self,new_dificulty=6):
        pass
        #return(self.empty)
    def place_num(self,x=0,y=0,num=1):

        formated_num=str(num)+"'"    
        self.playable[x,y]=formated_num.rstrip()
        #self.playable[x,y]=formated_num.rstrip()
        #self.playable[x,y]=num
        return(self.playable)
    def erase_entry(self,x=None, y=None):
        self.playable[x,y]='x'
        return(self.playable)
            
    def get_original(self):
        return(self.start.copy())
    def get_solution(self):
        return(self.solution.copy())
    def get_playable(self):
        return(self.playable.copy())
    def get_dificulty_index(self):
        return(self.dificulty_index)

    def print(self,tag='playable'):
        
        if tag=='solution':
            matrix=self.get_solution()
        if tag=='playable':
            matrix=self.get_playable()
        if tag=='original':
            matrix=self.get_original()

        return(matrix_format(matrix))


# A=Sudoku(9,10)
# while input()!= 'kkck':
#     #A.print('solution')
#     A.print('playable')
#     print('')
#     print('ponelo carajo')
#     E=input()
#     E=list(E)
#     kk=','
#     while(kk in E):
#         E.pop(E.index(','))
#     A.place_num(int(E[0]),int(E[1]),int(E[2]))
#     A.print('playable')
#     print('')
#     A.print('original')
#     print('')
#     print('kkck?')

