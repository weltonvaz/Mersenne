# np = ((2**n)-1)*(2*(n-1))
# 113589933
from sympy import divisor_count
for y in range(113000000,113000100):
    if divisor_count(y) == 2:
        print(y)