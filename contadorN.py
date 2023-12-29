import math

# variável com número muito grande
n = 1283
num = ((2**n)-1)

# determina o número de dígitos
num_digitos = math.floor(math.log10(num)) + 1

print("O número", num, "tem", num_digitos, "dígitos.")