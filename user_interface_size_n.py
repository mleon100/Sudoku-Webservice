from Controller_size_n import *
import time
from datetime import datetime

instrucciones= 'Bienvenido al juego de Sudoku, ingresa el nivel de dificultad. nivel 10 es el mas DIFICIL y 1 el mas FACIL'
print(instrucciones)
dificultad=int(input())

print('')
print('ingresa tamaño (size) de sudoku deseado')
size=abs(int(input()))

print('')
inicial_cond= game_initialicer(dificulty_filter(dificultad),size_filter(size))

alarm=None
absolute_time= datetime.now()

# main loop
while alarm!='qq':

    instant_time= datetime.now()
    local_time=instant_time-absolute_time
    print('TIME  ',local_time)
    # start of turn
    inicial_cond[0].print('playable')

    # user ending game option
    print('si quieres terminar el juego presiona la tecla "q", si deseas continuar presiona cualquier otra tecla')

    stop=str(input())
    if quit_game(stop,inicial_cond[0]):
        break
        
    print('')

    # original sudoku display option
    print('si deseas observar el sudoku antes de ser llenado presiona la tecla p, para continuar presiona cualquier otra tecla')

    original_sud= str(input())
    original_sud_display(original_sud,inicial_cond[0])
    
    
    # user input validation and procesing
    valid_input=False
    while not valid_input:
        
        print('ingresa un numero del 1 al 9 y una posicion (entre 1 y 9) que desees llenar. ej fila, columna, numero')
        user_input=input()

        try:
            valid_input=input_validation(user_input)
        except:
            print('Recuerda ingresar cantidad adecuada de numeros y no ingresar letras')

    

    user_input=input_preprocesing(user_input)

    # test sudoku rules
       
    if sudoku_rule_test(inicial_cond[0],inicial_cond[1],user_input):
        print('')
        print('respuesta valida')
        print('')
        #update
        inicial_cond[0].place_num(user_input[0]-1,user_input[1]-1,user_input[2])
    else:
        print('')
        print('numero o posicion invalida, intenta otra combinacion')
        print('')

    # completed game condition   
    if 'x' not in inicial_cond[0].playable:
        print('TIME  ',local_time)
        print('')
        print('Incognitas solucionadas: ',inicial_cond[0].get_dificulty_index())
        print('')
        print('GANASTE CTM!!!!')
        
        alarm='qq'

        
    
        


    
    