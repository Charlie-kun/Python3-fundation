import numpy as np
from tensorflow.keras.datasets import mnist
from keras.utils import np_utils

import sys
import tensorflow as tf

seed=0
np.random.seed(seed)
tf.random.set_seed(3)

(X_train, Y_class_train), (X_test, Y_class_test)=mnist.load_data()

print("Number of Learning set image : %d" %(X_train.shape[0]))
print("Number of Test set image : %d" %(X_test.shape[0]))

import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap="Greys")
plt.show()

for x in X_train[0]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')

X_train=X_train.reshape(X_train.shape[0], 784)
X_train=X_train.astype('float64')
X_train=X_train/255

X_train=X_test.reshape(X_test.shape[0], 784).astype('float64') / 255

print("class : %d" %(Y_class_train[0]))

Y_train=np_utils.to_categorical(Y_class_train,10)
Y_test=np_utils.to_categorical(Y_class_test, 10)

print(Y_train[0])
