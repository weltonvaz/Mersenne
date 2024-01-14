import sys
sys.set_int_max_str_digits(320000000)

import numpy as np

# Calcula o número
numero = (2**120237823) - 1

# Obtém o tamanho do número
tamanho = len(str(numero))

# Cria um ndarray de tamanho apropriado
array = np.zeros(tamanho, dtype=np.int64)

# Armazena os dígitos do número no ndarray
for i in range(tamanho):
    array[tamanho - i - 1] = int(numero % 10)
    numero //= 10

# Imprime o ndarray
# print(array)
