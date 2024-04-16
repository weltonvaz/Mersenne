import sys
sys.set_int_max_str_digits(10000)

import math

# variável com número muito grande
n = 467146949
num = ((2**n)-1)

# determina o número de dígitos
num_digitos = int(math.floor(math.log10(num)) + 1)

print(num_digitos, "dígitos.")