#class 26
import tensorflow as tf
import matplotlib.pyplot as plt

mnist=tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test)=mnist.load_data()
X_train,X_test=X_train/255.0, X_test/255.0
'''
plt.figure(figsize=(8,2))
for i in range(36):
    plt.subplot(3,12,i+1)
    plt.imshow(X_train[i],cmap="gray")
    plt.axis("off")
plt.show()

print(X_train.shape, X_train.dtype)
print(y_train.shape, y_train.dtype)
print(X_test.shape, X_test.dtype)
print(y_test.shape, y_test.dtype)
'''

model=tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),
                                  tf.keras.layers.Dense(1024, activation='relu'),
                                  tf.keras.layers.Dropout(0.3),
                                  tf.keras.layers.Dense(1024, activation='relu'),
                                  tf.keras.layers.Dropout(0.3),
                                  tf.keras.layers.Dense(1024, activation='relu'),
                                  tf.keras.layers.Dropout(0.3),
                                  tf.keras.layers.Dense(512, activation='relu'),
                                  tf.keras.layers.Dense(10, activation='softmax')
                                  ])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=["accuracy"])
model.summary()
hist=model.fit(X_train, y_train, validation_data=(X_test,y_test), verbose=2, batch_size=100, epochs=15, use_multiprocessing=True)
model.evaluate(X_test,y_test, verbose=2, batch_size=100,use_multiprocessing=True)

#Reporting
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.plot(hist.history['loss'])
plt.title("Cost Graph")
plt.ylabel("cost")
plt.subplot(1,2,2)
plt.title("Accuracy Graph")
plt.ylabel("accuracy")
plt.plot(hist.history['accuracy'], 'b-', label="training accuracy")
plt.plot(hist.history['val_accuracy'], 'r:', label="validation accuracy")
plt.legend()
plt.tight_layout()
plt.show()
