from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np 
import math

# x axis values
#x = np.linspace(-100,100,1000)
# corresponding y axis values

#def f (x): return 2*x**4 - 8*x**2 + 3


# plotting the points 
#plt.plot(x, f(x))
# giving a title to my graph
#plt.title('2x4 - 8x2 + 3 x[-2,2] Sección convexa')
#plt.title('2x4 - 8x2 + 3 x[-100,100]')
#plt.show()





#x = np.linspace(-100,100,1000)
#def f (x): return x**4 + 2*x**2 + 1

#plt.plot(x, f(x))

#plt.title('f (x) = x4+2x2+1  x[-1,1.3] ')
#plt.title('f (x) = x4+2x2+1  x[-100,100]')
#plt.show()



ax = plt.axes(projection="3d")

x_data = np.arange(-100,100,0.1)
y_data = np.arange(-100,100,0.1)
z_data = np.exp(x_data) +np.exp(y_data)-x_data-y_data

ax.scatter (x_data,y_data,z_data)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('f (x) = ex+ey-x-y  x[-100,100], y[-100,100]')

plt.show()
