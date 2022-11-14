import numpy as np 
import math
from sympy import *


# To declare symbol variables x and y 
from sympy import symbols

 #  You can't use numpy arrays for symbolical calculations with sympy. Instead, use a sympy Matrix
#    (https://stackoverflow.com/questions/68589864/matrix-determinant-symbolic-in-python)
import sympy 


# Declaring symbol variables x and y 
x = sympy.Symbol('x')
y = sympy.Symbol('y')



f = sympy.exp(x) + sympy.exp(y) -x -y 


# The first parameter of the diff function should be the function you want to take the derivative of. 
# The second parameter should be the variable you are taking the derivative with respect to.


dfx = f.diff(x)
print(dfx)

dfxX = f.diff(x,2)
print(dfxX)


dfy = f.diff(y)
print(dfy)

dfyy = f.diff(y,2)
print(dfyy)


dfy = f.diff(y)
print(dfy)

dfxy = dfy.diff(x)
print(dfxy)
