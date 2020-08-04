from Sudoku_toolbox_for_size_n import *
from Mformat_size_n import matrix_format




class Sudoku(object):
    def __init__(self,size=9,dificulty=6):
        self.sudoku= sudoku_creator(size,dificulty)
        self.start= self.sudoku[0]
        self.solution= self.sudoku[1]
        self.playable= self.start.copy()
        self.size=size
        self.dificulty_index=self.sudoku[2]
        
    
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



# K=input()
# K=list(K)
# kk=','
# while kk in K:
#     K.pop(K.index(','))
# print(K)

    
    
