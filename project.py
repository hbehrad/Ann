import numpy as np

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def binary_repr(n, width):
    return np.array(list(np.binary_repr(n, width=width))).astype(np.int8)

def generate_data(n_samples):
    X = np.random.randint(0, 1000, size=n_samples)
    y = np.array([is_even(x) for x in X])
    X = np.array([binary_repr(x, 10) for x in X])
    return X, y

X_train, y_train = generate_data(10000)
X_test, y_test = generate_data(1000)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(32, input_dim=10))
model.add(Dense(16))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=32)

score = model.evaluate(X_test, y_test)
print(score)
