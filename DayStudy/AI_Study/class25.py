import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np

xy_data = np.array([
    [1, 2, 1, 1, 2],
    [2, 1, 3, 2, 2],
    [3, 1, 3, 4, 2],
    [4, 1, 5, 5, 1],
    [1, 7, 5, 5, 1],
    [1, 2, 5, 6, 1],
    [1, 6, 6, 6, 0],
    [1, 7, 7, 7, 0]
])

x_data = xy_data[:, 0:-1]   # 0 ~ last slicing
y_data = xy_data[:, -1]     # just last
nb_classes = 3 # 0 ~ 2
print('x_data=\n', x_data)
print('y_data=\n', y_data)

Y_one_hot = tf.one_hot(y_data, nb_classes).numpy()
print('Y_one_hot=\n', Y_one_hot)

W = tf.Variable(tf.random.normal([4, nb_classes]), name='weight')
B = tf.Variable(tf.random.normal([nb_classes]), name='bias')

# define hypothesis
@tf.function
def Hypothesis(X):
    logits = tf.add(tf.matmul(tf.cast(X, tf.float32), W), B)
    return tf.nn.softmax(logits)

# define cost function
@tf.function
def loss(H, Y):
    entropy = -tf.reduce_sum(Y * tf.math.log(H), axis=1)
    # entropy = tf.losses.categorical_crossentropy(Y, H)
    cost = tf.reduce_mean(entropy)
    return cost

# minimize the cost function
@tf.function
def train(X, Y, learning_rate=0.1):
    with tf.GradientTape() as tape:
        _loss = loss(Hypothesis(X), Y)
    _w, _b = tape.gradient(_loss, [W, B])
    W.assign_sub(learning_rate * _w)
    B.assign_sub(learning_rate * _b)

# accuracy computation
@tf.function
def evaluation(H, Y):
    prediction = tf.argmax(H, 1)
    correct_prediction = tf.equal(prediction, tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return prediction, accuracy

# training...
for step in range(2001):
    _c = loss(Hypothesis(x_data), Y_one_hot)
    train(x_data, Y_one_hot, learning_rate=0.1)
    if step % 100 == 0:
        print(f"step:{step}\tloss:{_c.numpy()}")

# report accuracy...
print("\nAccuracy...")
_h = Hypothesis(x_data)
_p, _a = evaluation(_h, Y_one_hot)
print("Hypothesis =\n", _h.numpy())
print("Predicted =\n", _p.numpy())
print("\nAccuracy =", _a.numpy())

# testing...
test_data = np.array([
    [1, 2, 1, 1],
    [2, 1, 3, 2],
    [3, 1, 3, 4],
    [4, 1, 5, 5],
    [1, 7, 5, 5],
    [1, 2, 5, 6],
    [1, 6, 6, 6],
    [1, 7, 7, 7]
])
print("\ntesting...")
for data in test_data:
    result = tf.argmax(Hypothesis([data]), 1)
    print(f"input: {data}\t output: {result}")
