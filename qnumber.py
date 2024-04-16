n = 467
numero = ((2**n)-1)
contador = 0

while numero >= 1:
    contador += 1
    numero = numero // 10

print(contador)