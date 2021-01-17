'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import numpy as np
import tensorflow as tf

np.random.seed(3)
tf.random.set_seed(3)

Data_set=np.loadtxt("./data/dataset/ThoraricSurgery.csv", delimiter=",")

X=Data_set[:,0:17]
Y=Data_set[:,17]

model=Sequential()
model.add(Dense(30, input_dim=17, activation='relu'))
model.add(Dense(1, activation='relu'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X,Y, epochs=100, batch_size=10)
'''
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy
import tensorflow as tf

numpy.random.seed(3)
tf.random.set_seed(3)

dataset=numpy.loadtxt("./data/dataset/pima-indians-diabetes.csv", delimiter=",")
X=dataset[:,0:8]
Y=dataset[:,8]

model=Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X,Y, epochs=200, batch_size=5)

print("\n Accuracy : %.4f" % (model.evaluate(X,Y)[1]))
'''
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

np.random.seed(3)
tf.random.set_seed(3)

df=pd.read_csv('./data/dataset/iris.csv', names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

sns.pairplot(df, hue='species');
plt.show()

dataset = df.values
X = dataset[:,0:4].astype(float)
Y_obj = dataset[:,4]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
Y_encoded = tf.keras.utils.to_categorical(Y)

model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X,Y_encoded, epochs=50, batch_size=1)

print("\n Accuracy : %.4f" %(model.evaluate(X,Y_encoded)[1]))
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import numpy
import tensorflow as tf

numpy.random.seed(3)
tf.random.set_seed(3)

df = pd.read_csv('./data/dataset/sonar.csv', header=None)

dataset = df.values
X = dataset[:,0:60].astype(float)
Y_obj = dataset[:,60]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=200, batch_size=5)

print("\n Accuracy : %.4f" % (model.evaluate(X, Y)[1]))
