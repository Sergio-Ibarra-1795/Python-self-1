# importing Numpy package
import numpy as np

# To declare symbol variables x and y 
from sympy import symbols


 #  You can't use numpy arrays for symbolical calculations with sympy. Instead, use a sympy Matrix
#    (https://stackoverflow.com/questions/68589864/matrix-determinant-symbolic-in-python)
import sympy as sp


# creating a 3X3 Numpy matrix
n_array = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])
  
# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)
  
# calculating the determinant of matrix
det = np.linalg.det(n_array)
  
print("\nDeterminant of given 3X3 square matrix:")
print(int(det))




# FOR DETERMINANTS WITH SYMBOLS VARIABLES

# Problemas de clase 1 ejercicio 2

# Declaring symbol variables x and y 
x = sp.symbols('x')
y = sp.symbols('y')
z = sp.symbols('z')

# creating a 3X3 sp matrix
matrix = sp.Matrix(([1, x, x**2],
                    [1, y, y**2],
                    [1, z, z**2]))


# Displaying the Matrix
print("Matrix is:")
print(matrix)
  
# calculating the determinant of sp nmatrix
det3 = sp.det(matrix)
  
print("\nDeterminant of given 3X3 square matrix:")
print((det3))