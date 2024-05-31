from sympy import divisor_count
numero = 2**23
contador = 1
while contador < numero:
    if divisor_count(contador) == 2:
        print(contador)
    contador += 1