
import matplotlib.pyplot as plt
'''
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
'''

import numpy as np

'''
import time
n=1000
m=5000

X=np.random.rand(n,m)
W=np.random.rand(n,1)
Z=np.zeros((1,m))

start_time=time.time()

for i in range(X.shape[1]):
    for j in range(X.shape[0]):
        Z[0][i] +=W[j]+X[j][i]

end_time=time.time()

print("Loop use excute time : ", (end_time-start_time)*1000, "ms")

start_time=time.time()
Z=np.dot(W.T,X)
end_time=time.time()
print("Use numpy excute time : ", ((end_time-start_time)*1000), "ms")
'''

x=np.float32(1.0)

y=np.int_([1,2,4])

z=np.arange(3, dtype=np.uint8)

z.dtype

w=np.array([1,2,3], dtype='f')

x=np.array([2,3,1,0])

x=np.array([[1.+0.j,2.+0.j], [0.+0.j, 0.+0.j], [1.+1.j, 3.+0.j]])

x=np.array([[1,2.0], [0,0], (1+1j,3.)])

a=np.array([4,2,9,3])

print(a+1)

j=np.arange(5)
print(j)

print(2**(j+1)-j)

c=np.ones((3,3))

print(c.dot(c))

a=np.array([1,2,3,4])
b=np.array([4,2,2,4])
print(a==b)
print(a>b)
print(np.array_equal(a,b))

a=np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))

a=np.triu(np.ones((3,3)),0)
print(a)
print(a.T)

x=np.random.rand(2,2,2)
print("x=",x)

print(x.sum(axis=2)[0,1])

N=8
y=np.zeros(N)

x1=np.linspace(0,10,N, endpoint=True)
x2=np.linspace(0,10,N, endpoint=False)

plt.plot(x1, y, 'o')
plt.plot(x2, y+0.5, 'o')
plt.ylim([-0.5,1])
plt.show()

