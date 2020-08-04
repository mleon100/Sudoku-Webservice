import numpy as np
from numpy import random
import random

# returns matrix size*size filled with 'x'
def matrix_creator(size):
    # creas matrix size x size filled with 'x' values
    n= size**2
    
    matrix= np.array(['x ']*n)
    #matrix=np.array([int(0)]*n)
    matrix= matrix.reshape(size,size)
    return(matrix)

# returns a dictionary that maps matrix position starting at 1 to size, with a matrix index pair starting at [0,0] and ending at [size-1,size-1]
def position_mapping(size,pair_or_position):
    '''
    creates two dictionaries maping a position index ranging from 1 to size**2
    whith a ordered pair corresponding to a 2D matrix index.

    FOR ARGUMENT pair_or_position==0 the function returns pair_dict which takes 
    ordeted pairs as keys and position indexes as values

    FOR ARGUMENT pair_or_position==1 the function returns position_dict which 
    takes position indexes as keys and ordered pairs as values

    if pair_or_postion is not 0 or 1, the function will returns pair_dict by 
    default

    '''

    position_dict={}
    pair_dict={}
    k=1
    for i in range(size):
        for j in range(size):
            position_dict[k]=[i,j]
            pair_dict[i,j]=k
            k=k+1
    if pair_or_position==1:
        return position_dict
    else:
        return(pair_dict)

# creates a dictionary that maps submatrices to a sector index. This sectors/submatrices are of size  size**0.5 x size**0.5
def sector_mapping(size):
    '''
    returns dictionary maping sector position index (ranges from 1 to size)
    with submatrices of dimention= size**0.5 x size**0.5

    position indexes are keys and submatrices are values

    '''

    position_matrix_list=[]
    for i in range(size**2):
        position_matrix_list.append(i+1)
    
    position_matrix=np.array(position_matrix_list)
    sector_dict={}
    open_matrix = np.array_split(position_matrix,int(size**(1.5)))
    k=0
    
    key=1
    while k<int(size**0.5):

        # extrae size**0.5 matrices de size (filas) x size**0.5 (columnas), pone esta iformacion en una lista (suarray_list) que se renueva en cada ciclo
        subarray_list=[]
        for i in range(int(size**(1.5))):
            if i==k or ((i-k)%(size**0.5))==0:
                subarray_list.append(open_matrix[i])
        
        # print(subarray_list,k)
        # print('')

        # tomar de manera seguida size**0.5 elementos para formar submatrices de size**0.5 x size**0.5
        sub_matrix_list=[]
        j=1        
        while j<=size:
            sub_matrix_list.append(subarray_list[j-1])
            #print(sub_matrix_list,k)
            #print(j)
            
            if j%(size**0.5)==0:
                #print(sub_matrix_list,k,j)
                sub_matrix=np.array(sub_matrix_list)
                sub_matrix=sub_matrix.reshape(int(size**0.5),int(size**0.5))
                sector_dict[key]=sub_matrix
                key=key+1
                sub_matrix_list=[]
                #j=j+1
                
            j=j+1
           
        
        k=k+1
        
    return(sector_dict)


# returns true if matrix value at position_pair is valid acording to sudoku rules
def plane_search(matrix_temp,size,position):
    '''
    This function checks if the number that you want to introduce to the sudoku
    follows its rules.

    THE ARGUMENTS:
                    matrix_temp SHOULD be a copy of the original matrix
                    size is the size of the matrix
                    POSITION is the position index which varies in the range 1 to size**2
    '''


    #argumento matix debe ser una copia de la matriz originar debido a que se debe
    #alterar la matriz original solamente si esta funcion devuelve verdadero
    #print(position_mapping(size,1))


    position_pair=(position_mapping(size,1))[position]

    #limites de busqueda, depdnedientes de size solamente
    left= position_pair[1]
    right= size-position_pair[1]-1
    up= position_pair[0]
    down= size-position_pair[0]-1

    rowD_cond=False
    rowU_cond=False
    columnR_cond=False
    columnL_cond=False
    sector_cond=False

    # ROW ANALISIS searches in the rows of a column
    #border conditions
    if (down==0):
        rowD_cond=True
    if up==0:
        rowU_cond=True
    
    #general conditions
    row_counter=0
    for i in range(down):
        if matrix_temp[position_pair[0],position_pair[1]]== matrix_temp[position_pair[0]+i+1,position_pair[1]]:
            break
        else:
            row_counter=row_counter+1
        if row_counter==down:
            rowD_cond=True

    row_counter=0
    for i in range(up):
        if matrix_temp[position_pair[0],position_pair[1]]== matrix_temp[position_pair[0]-i-1,position_pair[1]]:
            break
        else:
            row_counter=row_counter+1
        if row_counter==up:
            rowU_cond=True
    
    # print('row ', rowD_cond and rowU_cond)
    # COLUMN ANALISIS searches in the columns of a row

    #border conditions
    if right==0:
        columnR_cond=True

    if left==0:
        columnL_cond=True
    
    #general conditions
    col_counter=0
    for j in range(right):
        if matrix_temp[position_pair[0],position_pair[1]]== matrix_temp[position_pair[0],position_pair[1]+j+1]:
            break
        else:
            col_counter=col_counter+1
        if col_counter==right:
            columnR_cond=True

    col_counter=0
    for j in range(left):
        if matrix_temp[position_pair[0],position_pair[1]]== matrix_temp[position_pair[0],position_pair[1]-j-1]:
            break
        else:
            col_counter=col_counter+1
        if col_counter==left:
            columnL_cond=True
    
    # print('col ', columnL_cond and columnR_cond)
    #sector analisis
      
    for i in range(size):
        if position in (sector_mapping(size))[i+1]:

            #sector is a submatrix
            sector=(sector_mapping(size))[i+1]
            break
    sector_positions=sector.flatten()
    sector_counter=0
    test_input_number=matrix_temp[position_pair[0],position_pair[1]]
    #print(test_input_number)

    for j in range(size):
                
        test_sector_number=matrix_temp[(position_mapping(size,1))[sector_positions[j]][0],(position_mapping(size,1))[sector_positions[j]][1]]
       # print((position_mapping(size,1))[sector_positions[j]])
        #print(test_input_number, test_sector_number)

        if (test_input_number== test_sector_number) and (position!=sector_positions[j]):
            break
        sector_counter=sector_counter+1
        if sector_counter==size:
            sector_cond=True
    # print('sector ', sector_cond)
    
    #final evaluation of conditions
    if (rowU_cond and rowD_cond and columnL_cond and columnR_cond and sector_cond):
        return True
    else:
        return False
        






    #intentar incluir busqueda por sector, si se puede chch


# creates a matrix that places the values 1 to 9 at random positions without repetition, and of SIZE n x n where n= size (variable=variable)**0.5
def random_submatrix_creator(size):
    
    sub_size=int(size**0.5)
    submatrix=matrix_creator(sub_size)
    position_dict=position_mapping(sub_size,1)

    posible_num=[0]*size
    for i in range(size):
        posible_num[i]=i+1
    #print(posible_num)
    
    posible_position=[0]*(size)
    for i in range(size):
        posible_position[i]=i+1
    
    pending_num=posible_num
    pending_position=posible_position
    

    while 'x ' in submatrix:
        test_position= random.choice(pending_position)
        test_num=random.choice(pending_num)
        # print(pending_num)
        # print(test_num)

        submatrix[position_dict[test_position][0],position_dict[test_position][1]]=test_num
        # print(submatrix)
        
        pending_num_index= pending_num.index(test_num)
        pending_position_index= pending_position.index(test_position)

        pending_num.pop(pending_num_index)
        pending_position.pop(pending_position_index)
    # print(submatrix)
    return(submatrix.copy())

# creates a changed copy of the submatrix from order or rows (row1,row2,row3) to (row2,row3,row1)
def row_shuffler(submatrix):
    

    shuffled_matrix=submatrix.copy()
    n=int(len(submatrix))
    
    row_temp=['x']*n
    # just saves the first row of the submatrix
    for k in range(n):
        row_temp[k]=submatrix[0,k]

    # navegates donwwards to consecutive rows
    for i in range(n):
        for j in range(n):
            if i== n-1:
                shuffled_matrix[i,j]=row_temp[j]
            else:
                
                #shuffled_matrix[i,j]=submatrix[n+i-2,j]
                shuffled_matrix[i,j]=submatrix[i+1,j]
    return shuffled_matrix

# creates a changed copy of the submatrix from order or columns (col1,col2,col3) to (col2,col3,col1)
def col_shuffler(submatrix):
    shuffled_matrix=submatrix.copy()
    n=int(len(submatrix))
    
    
    col_temp=['x']*n
    #just saves the first column of the submatrix
    for k in range(n):
        col_temp[k]=submatrix[k,0]
    
    # navegates to the righ to consecutive columns
    for i in range(n):
        for j in range(n):
            if i== n-1:
                shuffled_matrix[j,i]=col_temp[j]
            else:
                
                #shuffled_matrix[j,i]=submatrix[j,n+i-2]
                shuffled_matrix[j,i]=submatrix[j,i+1]
    return shuffled_matrix

# creates a size x size solved sudoku
def sudoku_solution_creator(size):
    n=int(size**0.5)

    #sector 1, all sudoku will be created from this one
    sub=random_submatrix_creator(size)
    # print(sub)
    # print('')
    sub_temp=sub.copy()
    # list containing all sectors, there are size number of sectors
    sectors=['o']*size

    # sector from 1 to size**0.5 are asigned to the list    
    for j in range(n):
        if j==0:
            sectors[j]= sub_temp
        else:
            A=sectors[j-1].copy()
            sectors[j]= col_shuffler(A)

    # the rest of the sectors are created and asigned using sectors 1 to size**0.5 as reference
    for j in range(n-1):
        for i in range(n):
            B=sectors[i+(n*j)].copy()
            sectors[i+(n*(j+1))]=row_shuffler(B)

    # creates list with numbers corresponding to the values (sector-1) for the first row of submatrices [0,3,6] for standard sudoku
    filling_reference_list=[]
    for i in range(size):
        if (i%n)==0:
            filling_reference_list.append(i)
    
    # fills the flat_sudoku (1D array) with flattend sectors by rows, submatrix by submatrix from left to right
    flat_sudoku= np.array([])
    for j in range(n):
        for i in range(n):
            C=sectors[j+filling_reference_list[i]]
            flat_sudoku=np.concatenate([flat_sudoku,C.flat])
    
    sudoku= flat_sudoku.reshape(size,size)

    return(sudoku)

# creates a playable sudoku from a solved sudoku
def sudoku_creator(size,dificulty):
    '''
    inicializes a sudoku of size=size 

    Returns a TUPLE of size 2, where:
    FIRST item is the UNSOLVED sudoku
    SECOND item is the SOLVED sudoku
    '''
    
    #difuculty is directly proportional to the number of numbers that will be subtracted from a solved sudoku
    #dificulty_index={1:44,2:46,3:48,4:50,5:52,6:54,7:56,8:58,9:60,10:62}
    #dificulty_index={1:2,2:46,3:48,4:50,5:52,6:54,7:56,8:58,9:59,10:64}
    dificulty_index={}
    #max_dif= int(((size**2)*63/81)//1) +1
    dif_step= int(((size**2)*5/81)//1)
    min_dif=int(((size**2)*18/81)//1)+1

    for i in range(1,11,1):
        dificulty_index[i]= min_dif+((i-1)*dif_step)

    #print(dificulty_index)

        
    #creates a list of al the positions (1<=positions<=size**2)
    posible_position=[0]*(size**2)
    for i in range(size**2):
        posible_position[i]=i+1

    #sudoku inicialization
    filled_sudoku=sudoku_solution_creator(size)
    unfilled_sudoku=filled_sudoku.copy()
    # print(filled_sudoku)
    # print('')
   
    filling_counter=0

    tested_positions=[]
   
    while filling_counter<dificulty_index[dificulty]:
                
        test_position=random.choice(posible_position)
        
        if (test_position not in tested_positions):
            tested_positions.append(test_position)
            unfilled_sudoku[(position_mapping(size,1))[test_position][0],(position_mapping(size,1))[test_position][1]]='x'
            filling_counter=filling_counter+1
               
    return(unfilled_sudoku,filled_sudoku,dificulty_index[dificulty])


# dificulty=1
# A=sudoku_creator(4,dificulty)
# print(A[1])
# print('')
# print(A[0])
# print(A[2])




    



