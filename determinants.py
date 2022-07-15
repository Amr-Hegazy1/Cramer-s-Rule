import numpy as np
from Matrices import get_first_nonzero_element,row_scalar_multiplication,row_addition

def det(matrix):
    if not is_square(matrix):
        raise ValueError("Must be square matrix")
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    elif has_zero_row(matrix) or has_zero_row(matrix.T):
        return 0
    else:
        matrix,k = det_echelon_form(matrix)
        res = 0
        for i in range(len(matrix)):
            if i % 2 == 0:
                res += matrix[0][i] * det(np.delete(matrix,i,1)[1:])
            else:
                res -= matrix[0][i] * det(np.delete(matrix,i,1)[1:])
        return res * k
def is_square(matrix):

    for row in matrix:
        if len(row) != len(matrix):
            return False
    return True

def sort_matrix(matrix):
    k = 1
    nonzero_indexes = [get_first_nonzero_element(row) for row in matrix] # the nonzero index represents the row that each row should be positioned at
    
    out_matrix = np.empty((len(matrix),len(matrix[0]),))
    out_matrix[:] = np.nan
    min_index = min(nonzero_indexes) # get min to be able to still work if there is no number in the first column in any row

    for i in range(len(nonzero_indexes)):
        relative_index = nonzero_indexes[i] - min_index
        
        if relative_index != len(matrix):
            while not np.isnan(out_matrix[relative_index]).any():
                relative_index += 1
        else:
            relative_index = -1
            while not np.isnan(out_matrix[relative_index]).any():
                relative_index -= 1
        if relative_index != i:
            k *= -1
        
        out_matrix[relative_index] = matrix[i]
            
            
        
    
    
    return [out_matrix,k]

def det_echelon_form(matrix):
    k = 1
    for i in range(len(matrix)):
        temp = sort_matrix(matrix)
        matrix = temp[0]
        
        k *= temp[1]
        nonzero_indexi = get_first_nonzero_element(matrix[i])
        if nonzero_indexi != len(matrix[i]):
            k *= matrix[i][nonzero_indexi]
            matrix[i] = row_scalar_multiplication(matrix[i],matrix[i][nonzero_indexi])
            for j in range(i+1,len(matrix)):
                nonzero_indexj = get_first_nonzero_element(matrix[j])
                if nonzero_indexj != len(matrix[i]) and nonzero_indexj == nonzero_indexi:
                    
                    matrix[j] = row_addition(matrix[i],matrix[j],matrix[j][nonzero_indexj])
                    
                
    nonzero_index = get_first_nonzero_element(matrix[-1])
    if nonzero_index != len(matrix[-1]):
        k *= matrix[-1][nonzero_index]
        matrix[-1] = row_scalar_multiplication(matrix[-1],matrix[-1][nonzero_index])
    
    
    
    return matrix,k
    
def has_zero_row(matrix):
    for row in matrix:
        if np.count_nonzero(row) == len(row):
            return True
    return False