from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np 
import math


x = np.linspace(-1.5,1.5,100)


def f (x): return 2*x**4-8*x**2+3


plt.plot(x, f(x))

plt.title('f(x) = 2x4- 8x2+3  x[-2,2] Zoom en sección convexa')
#plt.title('2x4 - 8x2 + 3 x[-100,100]')
plt.show()
