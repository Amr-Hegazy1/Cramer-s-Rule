import numpy as np
import copy
coefficent_matrix = np.array([[2,3,8],
                              [5,7,9],
                              [0,3,6]
                              ],dtype=float)

b_matrix = np.array([1,4,6],dtype=float)

try:
    coefficent_det = np.linalg.det(coefficent_matrix)
    if coefficent_det != 0: # det(A) != 0 for cramer's rule to work as it only computes unique solutions
        for i in range(len(coefficent_matrix)):
            coefficent_matrix_copy = copy.deepcopy(coefficent_matrix)
            coefficent_matrix_copy[:,i] = b_matrix.T
            augmented_det = np.linalg.det(coefficent_matrix_copy)
            print(f"Var {i+1} = {augmented_det/coefficent_det}")
    else:
        print("Cramer's rule can't compute a solution for such a system")
        
        
        
    
except np.linalg.LinAlgError:
    print("Must be square matrix")