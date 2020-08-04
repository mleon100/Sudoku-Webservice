from sudoku_size_n import*
import time
from datetime import datetime


# makes sure dificulty is in a range from 1 to 10, returns validated value of input
def dificulty_filter (dificultad):
    while dificultad not in range(1,11,1):
        print('ingresa un numero del 1 al 10')
        dificultad=int(input())
    return(dificultad)

# makes sure size= n^2 where n is a positive integer
def size_filter(size):
    while ((size**0.5)%1)!=0:
        print('recuerda que size= n^2 siendo n un entero')
        size=abs(int(input()))
        
    return(size)
    
  
# creates sudoku by callig object sudoku constructor, returns tuple. game_initialicer[0]= object sudoku, game_initializer[1]=size 
def game_initialicer(dificultad,size):
    
    S=Sudoku(size,dificultad)
       
    return(S,size)

# generates conditions for getting out of main loop
def quit_game(stop,S):
    out=False
    if stop=='q':
        print('seguro que deseas terminar el juego?')
        print('presiona "q" para salir, o cualquier otra tecla para continuar con el juego')
        answer=str(input())
        if answer=='q':
            print('JUEGO FINALIZADO')
            print('')
            print('Una solucion era')
            S.print('solution')
            out=True
    return(out)

# displays object sudoku's 'original' atribute under specified conditions
def original_sud_display(original_sud,S):
    if original_sud=='p':
        S.print('original')
    return()

# validates user input for correct logic working, returns bool
def input_validation(user_input):
    user_input=list(user_input)
    eliminate= ','

    while eliminate in user_input:
        user_input.pop(user_input.index(','))
    
    for i in range(len(user_input)):
        user_input[i]=int(user_input[i])
        user_input[i]= abs(user_input[i])
        
    
    if len(user_input)!=3:
        print('debes ingresar solamente tres numeros. ej: 1, 5, 7')
    else:
        a=user_input[0]//10==0
        b=user_input[1]//10==0
        c=user_input[2]//10==0

        if a and b and c:
            if user_input[0]==0 or user_input[1]==0 or user_input[2]==0:
                print('numero o posiciones no pueden ser 0. Escoge cifras entre 1 y 9')
            else:
                valid_input=True
    return(valid_input)

# changes a raw input into a list (indexable)
def input_preprocesing(user_input):
    user_input=list(user_input)
    eliminate= ','

    while eliminate in user_input:
        user_input.pop(user_input.index(','))
    
    for i in range(len(user_input)):
        user_input[i]=int(user_input[i])
        user_input[i]= abs(user_input[i])
    return(user_input)

# verifies sudoku rules, returns bool
def sudoku_rule_test(S,size,user_input):
    test_matrix=S.get_playable()
    test_matrix[user_input[0]-1,user_input[1]-1]= user_input[2]
    test_position= position_mapping(size,0)[(user_input[0]-1,user_input[1]-1)]

    valid=False

    
    if (S.get_playable()[user_input[0]-1,user_input[1]-1] =='x') and (plane_search(test_matrix,size,test_position)):
        valid=True
    return(valid)








# def sudoku_update(S):
#     completed=False

#     S.place_num(user_input[0]-1,user_input[1]-1,user_input[2])

#     if 'x' not in S.playable:
#         completed=True
#     return(completed)






        
    
        


    
    