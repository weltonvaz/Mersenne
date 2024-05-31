from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Suponha que 'dados' são seus dados de entrada e 'rotulos' são seus rótulos de saída
dados = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rotulos = np.array([1, 2, 2, 3, 2, 4, 2, 4, 3, 4])  # A quantidade de divisores para cada número em 'dados'

# Normalizar os dados
dados = dados / np.max(dados)
rotulos = rotulos / np.max(rotulos)

# Criar o modelo
modelo = Sequential()
modelo.add(Dense(64, input_dim=1, activation='relu'))
modelo.add(Dense(64, activation='relu'))
modelo.add(Dense(1, activation='linear'))

# Compilar o modelo
modelo.compile(loss='mean_squared_error', optimizer='adam')

# Treinar o modelo
modelo.fit(dados, rotulos, epochs=50, batch_size=1)

# Agora você pode usar o modelo para prever a quantidade de divisores para um novo número
novo_numero = 2047 / np.max(dados)  # Lembre-se de normalizar o novo número
predicao = modelo.predict(np.array([novo_numero]))
print(predicao * np.max(rotulos))  # Desnormalizar a predição
