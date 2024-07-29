def lucas_lehmer(p):
    """
    Verifica se o número de Mersenne 2^p - 1 é primo usando o teste de Lucas-Lehmer.
    """
    M = 2**p - 1
    s = 4

    for _ in range(p - 2):
        s = (s * s - 2) % M

    return s == 0

# Exemplo: Verificando se M_7 (2^7 - 1) é primo
if lucas_lehmer(523263):
    print(" é primo!")
else:
    print(" não é primo.")
