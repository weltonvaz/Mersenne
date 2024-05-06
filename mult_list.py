from functools import reduce
import operator

lista = [1, 2, 4, 8, 16, 32, 47]
resultado = reduce(operator.mul, lista)

print(resultado)  # Saída: 120
