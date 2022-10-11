import numpy as np
from sympy import symbols, hessian, Function, N, simplify, Matrix
import sympy as sp


# TAREA 2 EJERCICO 2A

x, y, z, a = symbols('x y z a')
f = symbols('f', cls=Function)

f1 = x**3 + 3*x -y**3

H = hessian(f1, [x, y])
print('Hessian matrix of the function f is:')
print(np.array(H))

# TO CALCULATE THE DETERMINANT
# creating a 3X3 sp matrix (Hessian)
Hessian = sp.Matrix(([6*x,0],
                    [0, -6*y]))
  
# calculating the determinant of sp matrix (Hessian)
det = sp.det(Hessian)
print("\nDeterminant of given 3X3 square matrix:")
print((det))
