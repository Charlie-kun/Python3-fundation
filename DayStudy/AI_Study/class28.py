#class 28
import numpy as np

X0_batch=np.array([[0,1,2],
                   [3,4,5],
                   [6,7,8],
                   [9,0,1]], dtype=np.float32)

X1_batch=np.array([[9,8,7],
                   [3,4,5],
                   [6,5,4],
                   [3,2,1]], dtype=np.float32)

print(f"X0_batch = {X0_batch.shape}")
print(f"X1_batch = {X1_batch.shape}")

import tensorflow as tf

hidden_size=2

Wx=tf.Variable(tf.random.normal([3,hidden_size], dtype=tf.float32))
Wy=tf.Variable(tf.random.normal([hidden_size,hidden_size], dtype=tf.float32))
b=tf.Variable(tf.zeros([1,hidden_size], dtype=tf.float32))

@tf.function
def run(X0,X1):
    Y0=tf.tanh(tf.matmul(X0,Wx)+b)
    Y1 = tf.tanh(tf.matmul(Y0, Wy) + tf.matmul(X1,Wx)+b)
    return Y0, Y1

_Y0, _Y1=run(X0_batch,X1_batch)
print(f"Y0:{_Y0.shape}\n{_Y0}")
print(f"Y1:{_Y1.shape}\n{_Y1}")
