import numpy as np

def mean_squared_error(y,t):
  return 0.5*np.sum((y-t)**2)

#one-hot incoding
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]   #Correct answer is '2'
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]    #Most guess big percentage is '2'.(0.6)
print(mean_squared_error(np.array(y), np.array(t)))   #Print at error percentage.

y=[0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]    #Most guess big percentage is '7'. (0.6)
print(mean_squared_error(np.array(y), np.array(t)))    #Print at error percentage.
