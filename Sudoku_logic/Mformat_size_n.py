from Sudoku_toolbox_for_size_n import *


# gives a fomrat to a matrix
def matrix_format(matrix):
    size= int((matrix.size)**0.5)
    sub_size=int(size**0.5)

    # formtat construction
    sud_format_bulk=[]
    sud_format_limit_ext=['||']
    for i in range(1,size+1,1):
        if i==1:
            sud_format_bulk.append('||  {:4}')
            
        elif (i-1)%sub_size==0:
            sud_format_bulk.append('|  {:4}')
            
        elif i==size:
            sud_format_bulk.append(':  {:4}||')
            
        else:
            sud_format_bulk.append(':  {:4}')
            
    sud_format_bulk=''.join(sud_format_bulk)
    sud_format_limit=['=']*(len(sud_format_bulk)-4)
    sud_format_limit=sud_format_limit_ext+sud_format_limit+sud_format_limit_ext
    sud_format_limit=''.join(sud_format_limit)


    # format aplication
    temp= matrix.copy()
    flat_sudoku= temp.flat
    line_list=[]
    
    print(sud_format_limit)
    for i  in range(size):
        for j in range(size):
            line_list.append(flat_sudoku[j+(i*size)])
        
        print(sud_format_bulk.format(*line_list))
        line_list=[]
        if (i+1)%sub_size==0:
            
            print(sud_format_limit)
            
    
    
    return()

# A=sudoku_creator(4,1)
# matrix_format(A[0])
# print('')
# matrix_format(A[1])
# # B=None
# # matrix_format(B)
