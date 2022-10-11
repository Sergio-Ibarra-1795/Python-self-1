from pydoc import doc
import numpy as np 
from sympy import symbols

matrizA = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrizA)
matrizB = np.array([[9],
                   [10],
                   [11]])
print(matrizB)

matrizC = matrizA.dot(matrizB)
print(matrizC)


B = np.array([[2,0,1],[1,0,1],[1,-1,2]])
print(B)

B_tra = B.transpose()
print(B_tra)


try:
    B_inv = np.linalg.inv(B)
    print(B_inv)
except:
    print("Singular Matrix, Inverse not possible.")



# To calculate final coeficient matrix
A = np.array([[2,1,1,0,0,0],[1,1,0,1,0,0],[1,2,0,0,-1,1]])
print(A)

orange = B_inv.dot(A)
print(orange)


# To calculate results vector

b = np.array([20,18,12])
resultados = B_inv.dot(b)
print(resultados)



# To calculate max or min

cb = np.array([5,0,4])
max_min_anterior = cb.dot(B_inv)
print(max_min_anterior)

max_min_def = max_min_anterior.dot(b)

print(max_min_def)



# To calculate Z resultante

M = symbols('M')
C = np.array([5,4,0,0,0,-M])
print(C)

Z_res1 = cb.dot(B_inv)
print(Z_res1)

Z_res2 = Z_res1.dot(A)
print(Z_res2)

Z_resultante = Z_res2.dot(C)
print(Z_resultante)

