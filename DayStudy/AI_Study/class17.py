# 17class
'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import tensorflow as tf

scalar=tf.constant(100)
vector=tf.constant([1,2,3,4,5])
matrix=tf.constant([[1,2,3],[4,5,6]])
cube=tf.constant([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])

print(scalar.get_shape())
print(vector.get_shape())
print(matrix.get_shape())
print(cube.get_shape())
print()
print(f"scalar={scalar}")
print(f"vector={vector}")
print(f"matrix=\n{matrix}")
print(f"cube=\n{cube}")
'''
'''
import tensorflow as tf

x=tf.Variable([1,2,3])
print(f"x=\n{x.numpy()}")

y=tf.zeros([3,4],dtype=tf.int32)
print(f"y=\n{y.numpy()}")

z=tf.fill([3,4],7)
print(f"z=\n{z}")
'''
'''
import tensorflow as tf
y1=tf.linspace(10.0, 20.0, 3, name='y1')
y2=tf.range(3, 18, 3, tf.int32, name='y2')
y3=tf.range(3, 1, -0.5, tf.float32, name='y3')

print(f"linspace=\n{y1.numpy()}\n")
print(f"range=\n{y2.numpy()}\n")
print(f"range=\n{y3.numpy()}")
'''
'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import tensorflow as tf

z1=tf.random.normal([2,3],-1,4)     #mean=-1, stddev=4
z2=tf.random.uniform([2,3],1,9)     #mein=1, max=9

print(f"random.normal = \n{z1.numpy()}")
print(f"random.uniform = \n{z2.numpy()}")
'''
'''
import tensorflow as tf

def myGradient(x):
    with tf.GradientTape() as tape:
        tape.watch(x)

        y=tf.multiply(2.0,tf.pow(x,2.0))    #y=2*x**2
    return tape.gradient(y,x).numpy()

a=myGradient(tf.constant(1.0))
b=myGradient(tf.constant(3.0))

print(a)
print(b)
'''

