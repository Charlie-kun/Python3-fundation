from tensorflow.keras.datasets import mnist
from keras.utils import np_utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import matplotlib.pyplot as plt
import numpy
import os
import tensorflow as tf

seed=0
numpy.random.seed(seed)
tf.random.set_seed(3)

(X_train, Y_Train), (X_test, Y_test)=mnist.load_data()

X_train=X_train.reshape(X_train.shape[0], 784).astype('float32') / 255
X_test=X_test.reshape(X_test.shape[0], 784).astype('float32') / 255

Y_Train=np_utils.to_categorical(Y_Train, 10)
Y_test=np_utils.to_categorical(Y_test, 10)

model=Sequential()
model.add(Dense(512, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

MODEL_DIR='./model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer=ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
eary_stopping_callback=EarlyStopping(monitor='val_loss', patience=10)

history=model.fit(X_train, Y_Train, validation_data=(X_test, Y_test), epochs=30, batch_size=200, verbose=0, callbacks=[eary_stopping_callback, checkpointer])

print("\n Test Accuracy : %.4f" % (model.evaluate(X_test, Y_test)[1]))

y_vloss=history.history['val_loss']

y_loss=history.history['loss']

x_len=numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

plt.legend(loc='upper right')

plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
