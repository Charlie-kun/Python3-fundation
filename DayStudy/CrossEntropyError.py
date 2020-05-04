import numpy as np

def cross_entropy_error(y,t):
  delta = 1e-7
  return -np.sum(t*np.log(y+delta))

#one-hot incoding
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]   #Correct answer is '2'
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]    #Most guess big percentage is '2'.(0.6)
print(cross_entropy_error(np.array(y), np.array(t)))   #Small error is good data.

y=[0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]    #Most guess big percentage is '7'. (0.6)
print(cross_entropy_error(np.array(y), np.array(t)))    #Result is bigger than answer '2'.
