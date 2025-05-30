#####Modelo de inteligencia artificial que realice cuatro operaciones basicas que son suma, resta, multiplicacion y division#######
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import tensorflow as tf

#Suma, resta, multiplicacion y division
operaciones = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y if y != 0 else 0
}

X = []
y = []

for op in range(4):
    for i in range(10):
        for j in range(10):
            if op == 3 and j == 0:
                continue
            X.append([i, j, op])
            y.append(operaciones[op](i, j))

X = np.array(X, dtype=np.float32)
y = np.array(y, dtype=np.float32)

X /= 9.0
y_max = np.max(y)
y /= y_max

model = Sequential([
    Input(shape=(3,)),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

hist = model.fit(X, y, epochs=1000, verbose=0)

def predecir(op1, op2, tipo_op):
    entrada = np.array([[op1, op2, tipo_op]], dtype=np.float32) / 9.0
    resultado_normalizado = model.predict(entrada, verbose=0)[0][0]
    return resultado_normalizado * y_max

#Ejecucion
simbolos = ['+', '-', '*', '/']
for op in range(4):
    print(f"\nOperación: {simbolos[op]}")
    for i in range(10):
        for j in range(10):
            if op == 3 and j == 0:
                continue
            pred = predecir(i, j, op)
            real = operaciones[op](i, j)
            print(f"{i} {simbolos[op]} {j} = {round(pred, 2)}")
