from sympy import divisors, divisor_count
n = 23
np = ((2**n)-1)*(2**(n-1))
divisors(np)
sp = sum(divisors(np)[:-1])

len(divisors(sp))
a = (divisors(sp))

(31+16)*2

from math import sqrt, lcm, gcd
# Comprimento da diagonal do lado a (a) (m)
a = 31

# Comprimento da diagonal do lado b (b) (m)
b = 16

# comprimento diagonal (q)(m)
q = sqrt((a*a)+(b*b))

# Calculando a Area do Retangulo (S)(sq.m)
S = a * b

#Perimetro (P)(m)
P = 2 * (a+b)

# DIVISORES de P2096128
P2096128 = [1, 2, 4, 8, 16, 23, 32, 46, 64, 89, 92, 128, 178, 184, 256, 356, 368, 512, 712, 736, 1024, 1424, 1472, 2047, 2848, 2944, 4094, 5696, 5888, 8188, 11392, 11776, 16376, 22784, 23552, 32752, 45568, 65504, 91136, 131008, 262016, 524032, 1048064, 2096128]
         
# DIVISORES de P2325392
P2325392 = [1, 2, 4, 8, 16, 23, 46, 71, 89, 92, 142, 178, 184, 284, 356, 368, 568, 712, 1136, 1424, 1633, 2047, 3266, 4094, 6319, 6532, 8188, 12638, 13064, 16376, 25276, 26128, 32752, 50552, 101104, 145337, 290674, 581348, 1162696, 2325392]


# Encontrando a interseção dos dois conjuntos
a = set(P2096128)
b = set(P2325392)
c = intersecao = a & b

c = {1, 2, 4, 8, 16, 1424, 23, 46, 178, 184, 712, 89, 92, 356, 368, 32752, 16376, 8188, 4094, 2047}

int((2**0.5)+1)

primes = [num for num in range(2,128) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]