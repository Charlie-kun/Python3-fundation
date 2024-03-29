#1. Data
import numpy as np
x=np.array(range(1,101))
y=np.array(range(1,101))

# Divide at rate
x_train=x[:60] #6:2:2
x_val=x[60:80]
x_test=x[80:]

y_train=x[:60] #6:2:2
y_val=x[60:80]
y_test=x[80:]

#2. Model Configuration
from keras.models import Sequential
from keras.layers import Dense
model=Sequential()

model.add(Dense(5,input_dim=1, activation='relu'))
#model.add(Dense(5,imput_dim=(1,), activation='relu'))
model.add(Dense(3))
model.add(Dense(4))
model.add(Dense(1))

#model.summary()

#3. Training
#model.complie(loss='mse', optimizer='adam', metrics=['accuracy'])
model.compile(loss='mse', optimizer='adam', metrics=['mse'])
model.fit(x_train, y_train, epochs=1000, batch_size=1, validation_data=(x_val, y_val))

#4. Valutation Prediction
mse=model.evaluate(x_test, y_test, batch_size=1)
print("mse : ", mse)

y_predict=model.predict(x_test)
print(y_predict)

# Find RMSE
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE  : ", RMSE(y_test, y_predict))

# Find R2
from sklearn.metrics import r2_score
r2_y_predict=r2_score(y_test, y_predict)
print("R2 : ", r2_y_predict)
