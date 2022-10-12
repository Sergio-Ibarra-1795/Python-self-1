from pydoc import doc
import numpy as np 
from sympy import symbols


M, b1, b2, b3, c1 = symbols('M, b1, b2, b3, c1')

#A es la matriz de los coeficientes de las restricciones en la tabla simplex original, es decir, del problema original en su forma estandar 
A = np.array([[2,3,1,0,0],[1,2,0,-1,1]])
print('La matriz de coeficientes del problema original en forma estandar es:')
print(A)

# LA MATRIZ TRANSUPESTA DE A es:



#C son los valores de los coeficientes en la función objetivo (incluye slack, artificiales y de surplus)
print('El vector C de coeficientes de la función objetivo es:')
#Para maximo se resta M y para mínimo se suma M en C (función objetivo)
C = np.array([2,3,0,0,M])
print(C)

# b= Vector de valores de las restricciones
print('El vector de valores de la restricciones es:')
b = np.array([30,10])
print(b)


#Para conocer los valores de B, B-1 y CB es necesario conocer cuales son las variables básicas en la última tabla del tableau de simplex
#cb es el vector de coeficientes de valores de las bases en la función objetivo 
cb = np.array([0,3]) #s1 y x2 son las v básicas

# B son los coeficientes de la base (que quedó al final del simplex) en la tabla simplex original
B = np.array([[1,3],[0,2]])
print('La matriz de coeficientes de la base es:')
print(B)

# To calculate optimum value
# First we calculate B-1
try:
    B_inv = np.linalg.inv(B)
    print('La matriz INVERSA de coeficientes de la base B-1 es:')
    print(B_inv)
except:
    print("Singular Matrix, Inverse not possible.")

# Then we calculate optimum value =  Cb* B-1*b
valor_optimo_calculo_anterior = cb.dot(B_inv)
valor_optimo_def = valor_optimo_calculo_anterior.dot(b)
print('El valor optimo es:')
print(valor_optimo_def)

# To calculate final coeficient matrix
# Is the coeficiente matrix in the last tableau table 
last_coef_matrix = B_inv.dot(A)
print('La matriz de coeficientes del último tableau (óptimo) es:')
print(last_coef_matrix )


# To calculate results vector: B-1*b
#resultados son los valores que toman las variables basicas
vector_resultados = B_inv.dot(b)
print('El vector de resultados en la solución es:')
print(vector_resultados)


# To calculate vector Z resultante
Z_res1 = cb.dot(B_inv)
#print(Z_res1)
Z_res2 = Z_res1.dot(A)
#print(Z_res2)
Z_resultante = Z_res2 - C
print('El vector de coeficientes de la función objetivo en el último tableu (óptimo) es:')
print(Z_resultante)


# SENSITIVITY ANALYSIS 

# To determine shadow prices 

# Precio sombra de restricción 1 (valor de la primer variable en el dual)
b_shadow = np.array([b[0]+1,b[1]])
# To prove the impact of shadow prices In the b vector
resultados_shadow = B_inv.dot(b_shadow)
print('El vector de resultados en la solución cambiados al mover 1 unidad el valor de la restricicón 1 es:')
print(resultados_shadow)
# In max/min result 
max_min_anterior = cb.dot(B_inv)
max_min_shadow = max_min_anterior.dot(b_shadow)
print('El valor óptimo en la solución cambiado al mover 1 unidad el valor de la restricicón 1 es:')
print(max_min_shadow)
print('El precio sombra al mover 1 unidad el valor de la restricicón 1 es:')
print(abs((max_min_shadow)-valor_optimo_def))

# Precio sombra de restricción 2 (valor de la segunda variable en el dual)
b_shadow2 = np.array([b[0],b[1]+1])
# To prove the impact of shadow prices In the b vector
resultados_shadow2 = B_inv.dot(b_shadow2)
print('El vector de resultados en la solución cambiados al mover 1 unidad el valor de la restricicón 2 es:')
print(resultados_shadow2)
# In max/min result 
max_min_anterior = cb.dot(B_inv)
max_min_shadow2 = max_min_anterior.dot(b_shadow2)
print('El valor óptimo en la solución cambiado al mover 1 unidad el valor de la restricicón 2 es:')
print(max_min_shadow2)
print('El precio sombra al mover 1 unidad el valor de la restricicón 2 es:')
print(abs((max_min_shadow2)-valor_optimo_def))


#To determine values that can take coeficients in the objective function
print('El vector de coeficientes C para determinar un cambio en C1 es:')
C_prima = np.array([c1,5,0,0,0])
print(C_prima)
cb_prima = np.array([0,5,c1])

intermedio = cb_prima.dot(last_coef_matrix)
#print(intermedio)
intermedio2 = intermedio - C_prima
print('El vector de análisis de sensibilidad al cambiar C1 en función objetivo es:')
print(intermedio2)