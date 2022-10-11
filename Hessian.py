import numpy as np
from sympy import symbols, hessian, Function, N, simplify, Matrix
import sympy as sp


# TAREA 2 EJERCICO 2A

x, y, z, a = symbols('x y z a')
f = symbols('f', cls=Function)

f1 = 2*x**2 + 3*y**2 -a*z**2 + 4*x*y +3*y*z

H = hessian(f1, [x, y, z])
print('Hessian matrix of the function f is:')
print(np.array(H))

# TO CALCULATE THE DETERMINANT
# creating a 3X3 sp matrix (Hessian)
Hessian = sp.Matrix(([4, 4, 0],
                    [4, 6, 3],
                    [0, 3, -2*a]))
  
# calculating the determinant of sp matrix (Hessian)
det = sp.det(Hessian)
print("\nDeterminant of given 3X3 square matrix:")
print((det))



# TAREA 2 EJERCICO 2B
x, y, z, a, b = symbols('x y z a b')
f = symbols('f', cls=Function)

f2 = x**2 + 3*y**2 +a*z**2 -3*b*x*y

H2 = hessian(f2, [x, y, z])
print('Hessian matrix of the second function f is:')
print(np.array(H2))

# TO CALCULATE THE DETERMINANT
# Declaring symbol variables x and y 
a = sp.symbols('a')
b = sp.symbols('b')

# creating a 3X3 sp matrix
Hessian2 = sp.Matrix(([2, -3*b, 0],
                    [-3*b, 6, 0],
                    [0, 3, 2*a]))

# calculating the determinant of sp nmatrix
det2 = sp.det(Hessian2)
print("\nDeterminant of given 3X3 square matrix (Hessian2):")
print((det2))



# TAREA 2 EJERCICO 4
x, y = symbols('x y')
f = symbols('f', cls=Function)
f3 = (2+x)**2 + (y +x)**3

H3 = hessian(f3, [x, y])
print('Hessian matrix of the third function f is:')
print(np.array(H3))

# TO CALCULATE THE DETERMINANT
# creating a 3X3 sp matrix
Hessian3 = sp.Matrix(([6*x +6*y+2, 6*x +6*y],
                    [6*x +6*y, 6*x +6*y]))

# calculating the determinant of sp nmatrix
det3 = sp.det(Hessian3)
print("\nDeterminant of given 3X3 square matrix (Hessian3):")
print((det3))

