import numpy as np
import matplotlib.pylab as plt

def function_1(x):
  return 0.01*x**2+0.1*x

x= np.arange(0.0, 20.0, 0.1)
y=function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)

def numerical_diff(f,x):
  h=1e-4    #0.001
  return (f(x+h) - f(x-h)/2*h)

print(numerical_diff(function_1,5))    #0.74999825010999949
print(numerical_diff(function_1,10))    #1.9999300015999948

plt.show()

def function_2(x):
  return x[0]**2+x[1]**2

x= np.arange(0.0, 20.0, 0.1)
y=function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()
