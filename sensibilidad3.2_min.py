from pydoc import doc
import numpy as np 
from sympy import symbols

# B son los coeficientes de la base (que quedó al final del simplex) en la tabla simplex original
B = np.array([[1,1],[-2,2]])
print('La matriz de coeficientes de la base es:')
print(B)


try:
    B_inv = np.linalg.inv(B)
    print('La matriz INVERSA de coeficientes de la base B-1 es:')
    print(B_inv)
except:
    print("Singular Matrix, Inverse not possible.")



# To calculate final coeficient matrix

#A es los coeficientes de la tabla simplex original, es decir, del problema original en su forma estandar 
A = np.array([[-2,1,1,1,0],[1,-2,2,0,1]])

print('La matriz de coeficientes del problema original en forma estandar es:')
print(A)

# orange is the coeficiente matrix in the last tableau table 
orange = B_inv.dot(A)
print('La matriz de coeficientes del último tableau (óptimo) es:')
print(orange)


# To calculate results vector

# B= valores de las restricciones
print('El vector de valores de la restricciones es:')
b = np.array([4,2])
print(b)

#resultados son los valores que toman las variables basicas
resultados = B_inv.dot(b)
print('El vector de valores de las variables básicas en la solción es:')
print(resultados)

# To calculate max or min
#cb es el vector de coeficientes de valores de las bases en la función objetivo 
cb = np.array([1,1])
max_min_anterior = cb.dot(B_inv)
#print(max_min_anterior)
max_min_def = max_min_anterior.dot(b)
print('El valor optimo es:')
print(max_min_def)


# To calculate Z resultante
M, b1, b2, b3, c1 = symbols('M, b1, b2, b3, c1')

#C son los valores de los coeficientes en la función objetivo (incluye slack, artificiales y de surplus)
print('El vector C de coeficientes de la función objetivo es:')

#Para maximo se resta M y para mínimo se suma M en C (función objetivo)
C = np.array([-1,1,1,M,M])
print(C)
Z_res1 = cb.dot(B_inv)
#print(Z_res1)
Z_res2 = Z_res1.dot(A)
#print(Z_res2)
Z_resultante = Z_res2 - C
print('El vector de coeficientes de la función objetivo en el último tableu (óptimo) es:')
print(Z_resultante)



# To calculate sensibility analisis for b vector 
b1_prima = np.array([b1,2])
b1_sensbibilidad= B_inv.dot(b1_prima)
print('El vector de análisis de sensibilidad del primer restricción es:')
print(b1_sensbibilidad)

# To prove a new value in the constraint vector
b_prima_asignado = np.array([5,2])
resultados_sensibilidad1 = B_inv.dot(b_prima_asignado)
print('El vector de valores de las variables básicas en la solución (analisis de sensibilidad1) es:')
print(resultados_sensibilidad1)


max_min_anterior = cb.dot(B_inv)
max_min_def_sensibilidad1 = max_min_anterior.dot(b_prima_asignado)
print('El valor óptimo corregido por el nuevo valor en la restricicón 1 es:')
print(max_min_def_sensibilidad1)



# To determine shadow prices 
b_shadow = np.array([5,2])
# To prove the impact of shadow prices 
# In the b vector
resultados_shadow = B_inv.dot(b_shadow)
print('El vector de valores de las variables básicas en la solución cambiados al mover 1 unidad el valor de la restricicón 1 es:')
print(resultados_shadow)
# In max/min result 
max_min_anterior = cb.dot(B_inv)
max_min_shadow = max_min_anterior.dot(b_shadow)
print('El valor óptimo en la solución cambiado al mover 1 unidad el valor de la restricicón 1 es:')
print(max_min_shadow)
print('El precio sombra al mover 1 unidad el valor de la restricicón 1 es:')
print(abs((max_min_shadow)-max_min_def))



#To determine values that can take coeficients in the objective function
M, b1, b2, b3, c1 = symbols('M, b1, b2, b3, c1')
print('El vector de coeficientes C para determinar un cambio en C1 es:')
C_prima = np.array([c1,1,1,0,M,0,M,0,M])
print(C_prima)
cb_prima = np.array([c1,1,0])

intermedio = cb_prima.dot(orange)
#print(intermedio)
intermedio2 = intermedio - C_prima
print('El vector de análisis de sensibilidad al cambiar C1 en función objetivo es:')
print(intermedio2)